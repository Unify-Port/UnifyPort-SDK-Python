#!/usr/bin/env python3
"""Scan source trees and built archives for public-release safety issues."""

from __future__ import annotations

import argparse
import re
import stat
import sys
import tarfile
import zipfile
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRECTORIES = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "htmlcov",
}
TEXT_SUFFIXES = {
    "",
    ".cfg",
    ".css",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".lock",
    ".md",
    ".py",
    ".rst",
    ".toml",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
FORBIDDEN_NAMES = {
    ".env",
    ".npmrc",
    ".pypirc",
    "id_dsa",
    "id_ed25519",
    "id_rsa",
}
MAX_SCANNED_FILE_BYTES = 16 * 1024 * 1024


def _joined(*parts: str) -> str:
    # 规则字面量分段保存，避免扫描器源码被自身规则命中。
    return "".join(parts)


CONTENT_RULES = (
    (
        "private key material",
        re.compile(_joined("-----BEGIN ", "(?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ),
    (
        "well-known access token",
        re.compile(
            _joined(
                "(?:gh[pousr]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|",
                "npm_[A-Za-z0-9]{20,}|glpat-[A-Za-z0-9_-]{20,}|",
                "xox(?:a|b|p|r|s)-[A-Za-z0-9-]{20,})",
            )
        ),
    ),
    (
        "JSON Web Token",
        re.compile(
            _joined(
                "eyJ[A-Za-z0-9_-]{8,}\\.",
                "[A-Za-z0-9_-]{8,}\\.[A-Za-z0-9_-]{8,}",
            )
        ),
    ),
    (
        "production-looking Device API key",
        re.compile(r"\bdk_(?:live|prod)_[A-Za-z0-9_-]{20,}\b", re.IGNORECASE),
    ),
    (
        "hard-coded environment credential",
        re.compile(
            _joined(
                "(?:UNIFYPORT_DEVICE_API_KEY|API_KEY|PASSWORD|SECRET|TOKEN)",
                "\\s*=\\s*[\"']",
                "(?!<(?:api-key|password|secret|token)>|replace|example|changeme)",
                "[A-Za-z0-9_./+=:-]{16,}[\"']",
            ),
            re.IGNORECASE,
        ),
    ),
    (
        "macOS user home path",
        re.compile(_joined("/", "Users", "/[^/\\s]+/")),
    ),
    (
        "Linux user home path",
        re.compile(_joined("/", "home", "/[^/\\s]+/")),
    ),
    (
        "Windows user home path",
        re.compile(_joined("[A-Za-z]:\\\\", "Users", "\\\\[^\\\\s]+\\\\")),
    ),
    (
        "private network URL",
        re.compile(
            _joined(
                "https?://(?:10\\.[0-9.]+|192\\.168\\.[0-9.]+|",
                "172\\.(?:1[6-9]|2[0-9]|3[01])\\.[0-9.]+|",
                "[A-Za-z0-9.-]+\\.(?:corp|internal|lan|local))(?:[:/]|$)",
            ),
            re.IGNORECASE,
        ),
    ),
)


@dataclass(frozen=True, slots=True)
class Finding:
    file: str
    rule: str


@dataclass(frozen=True, slots=True)
class PublicFile:
    display_name: str
    content: bytes
    issues: tuple[str, ...] = ()


def _unsafe_archive_name(name: str) -> bool:
    normalized = PurePosixPath(name.replace("\\", "/"))
    return normalized.is_absolute() or ".." in normalized.parts


def _forbidden_name(name: str) -> bool:
    basename = PurePosixPath(name.replace("\\", "/")).name
    return (
        basename in FORBIDDEN_NAMES
        or basename.endswith((".key", ".pem", ".p12", ".pfx", ".pyc"))
        or basename == ".DS_Store"
    )


def _is_checker(name: str) -> bool:
    return name.replace("\\", "/").endswith("/scripts/check_public.py") or name == (
        "scripts/check_public.py"
    )


def _source_files(directory: Path) -> Iterator[PublicFile]:
    for path in sorted(directory.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(directory)
        if any(part in IGNORED_DIRECTORIES for part in relative.parts):
            continue
        yield PublicFile(relative.as_posix(), path.read_bytes())


def _zip_files(path: Path) -> Iterator[PublicFile]:
    with zipfile.ZipFile(path) as archive:
        for entry in archive.infolist():
            if entry.is_dir():
                continue
            if _unsafe_archive_name(entry.filename):
                yield PublicFile(entry.filename, b"")
                continue
            unix_mode = entry.external_attr >> 16
            if stat.S_ISLNK(unix_mode):
                yield PublicFile(entry.filename, b"", ("archive symlink",))
                continue
            if entry.flag_bits & 0x1:
                yield PublicFile(entry.filename, b"", ("encrypted archive entry",))
                continue
            if entry.file_size > MAX_SCANNED_FILE_BYTES:
                yield PublicFile(entry.filename, b"", ("file exceeds public scan byte limit",))
                continue
            yield PublicFile(entry.filename, archive.read(entry))


def _tar_files(path: Path) -> Iterator[PublicFile]:
    with tarfile.open(path, mode="r:*") as archive:
        for entry in archive.getmembers():
            if not entry.isfile():
                if entry.issym() or entry.islnk():
                    yield PublicFile(entry.name, b"", ("archive symlink",))
                continue
            if _unsafe_archive_name(entry.name):
                yield PublicFile(entry.name, b"")
                continue
            if entry.size > MAX_SCANNED_FILE_BYTES:
                yield PublicFile(entry.name, b"", ("file exceeds public scan byte limit",))
                continue
            extracted = archive.extractfile(entry)
            if extracted is None:
                yield PublicFile(entry.name, b"")
                continue
            yield PublicFile(entry.name, extracted.read())


def _public_files(path: Path) -> Iterator[PublicFile]:
    if path.is_dir():
        yield from _source_files(path)
        return
    lower_name = path.name.lower()
    if lower_name.endswith((".whl", ".zip")):
        yield from _zip_files(path)
        return
    if lower_name.endswith((".tar.gz", ".tgz", ".tar.bz2", ".tar.xz")):
        yield from _tar_files(path)
        return
    yield PublicFile(path.name, path.read_bytes())


def _scan_file(public_file: PublicFile) -> list[Finding]:
    findings = [Finding(public_file.display_name, issue) for issue in public_file.issues]
    name = public_file.display_name
    if _unsafe_archive_name(name):
        findings.append(Finding(name, "unsafe archive path"))
    if _forbidden_name(name):
        findings.append(Finding(name, "forbidden sensitive filename"))
    if len(public_file.content) > MAX_SCANNED_FILE_BYTES:
        findings.append(Finding(name, "file exceeds public scan byte limit"))
        return findings
    suffix = PurePosixPath(name).suffix.lower()
    if suffix not in TEXT_SUFFIXES or b"\x00" in public_file.content or _is_checker(name):
        return findings
    text = public_file.content.decode("utf-8", errors="replace")
    for label, pattern in CONTENT_RULES:
        if pattern.search(text):
            findings.append(Finding(name, label))
    return findings


def scan_public_paths(paths: Iterable[Path]) -> tuple[int, list[Finding]]:
    findings: list[Finding] = []
    scanned = 0
    for path in paths:
        if not path.exists():
            findings.append(Finding(path.name, "scan target is missing"))
            continue
        for public_file in _public_files(path):
            scanned += 1
            findings.extend(_scan_file(public_file))
    return scanned, findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    arguments = parser.parse_args()
    paths = [path.resolve() for path in arguments.paths] if arguments.paths else [ROOT]
    try:
        scanned, findings = scan_public_paths(paths)
    except (OSError, tarfile.TarError, zipfile.BadZipFile) as error:
        print(f"[public:check] unable to scan artifact: {type(error).__name__}", file=sys.stderr)
        return 1
    if findings:
        for finding in findings:
            print(f"[public:check] {finding.file}: {finding.rule}", file=sys.stderr)
        return 1
    print(f"[public:check] scanned {scanned} public files", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
