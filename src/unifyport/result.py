"""Decoded operation results without a raw HTTP response handle."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class ApiResult(Generic[T]):
    """Complete decoded API envelope and filtered response metadata."""

    data: T
    status: int
    request_id: str | None = None


__all__ = ["ApiResult"]
