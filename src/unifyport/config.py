"""Public client configuration with finite, security-oriented defaults."""

from __future__ import annotations

from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass, field
from typing import TypeAlias

DEFAULT_TIMEOUT = 30.0
DEFAULT_MAX_RETRIES = 2
DEFAULT_BASE_DELAY = 0.2
DEFAULT_MAX_DELAY = 5.0
DEFAULT_MAX_RESPONSE_BYTES = 8 * 1024 * 1024
MAX_RESPONSE_BYTES = 64 * 1024 * 1024
MAX_RETRIES = 10
MAX_TIMEOUT = 2_147_483.647

SyncCredentialProvider: TypeAlias = Callable[[], str | None]
AsyncCredentialProvider: TypeAlias = Callable[[], str | None | Awaitable[str | None]]
SyncSecretSource: TypeAlias = str | SyncCredentialProvider
AsyncSecretSource: TypeAlias = str | AsyncCredentialProvider
# 通用 alias 保留给 credential resolver；client 构造器使用更窄的 sync/async alias。
SecretSource: TypeAlias = AsyncSecretSource


@dataclass(frozen=True, slots=True)
class RetryConfig:
    """Automatic retry budget for operations explicitly marked retryable."""

    max_retries: int = DEFAULT_MAX_RETRIES
    base_delay: float = DEFAULT_BASE_DELAY
    max_delay: float = DEFAULT_MAX_DELAY


@dataclass(frozen=True, slots=True)
class RequestOptions:
    """Per-operation overrides that can only reduce client-wide budgets."""

    timeout: float | None = None
    max_retries: int | None = None
    retry: bool | None = None

    def __post_init__(self) -> None:
        # 两种 retry 写法只为兼容常见调用风格，同时出现会让收紧语义不明确。
        if self.max_retries is not None and self.retry is not None:
            raise ValueError("max_retries and retry cannot both be set")


@dataclass(frozen=True, slots=True, repr=False)
class DeviceClientConfig:
    """Configuration for :class:`UnifyPortDeviceClient`."""

    base_url: str
    api_key: SyncSecretSource = field(repr=False)
    timeout: float = DEFAULT_TIMEOUT
    retry: RetryConfig = field(default_factory=RetryConfig)
    max_response_bytes: int = DEFAULT_MAX_RESPONSE_BYTES
    allow_insecure_http: bool = False

    def __repr__(self) -> str:
        # config 可能在校验前被日志展开，因此 URL 与 credential 都不进入 repr。
        return (
            "DeviceClientConfig(base_url=<redacted>, api_key=<redacted>, "
            f"timeout={self.timeout!r}, retry={self.retry!r}, "
            f"max_response_bytes={self.max_response_bytes!r}, "
            f"allow_insecure_http={self.allow_insecure_http!r})"
        )


@dataclass(frozen=True, slots=True, repr=False)
class AsyncDeviceClientConfig:
    """Configuration for :class:`AsyncUnifyPortDeviceClient`."""

    base_url: str
    api_key: AsyncSecretSource = field(repr=False)
    timeout: float = DEFAULT_TIMEOUT
    retry: RetryConfig = field(default_factory=RetryConfig)
    max_response_bytes: int = DEFAULT_MAX_RESPONSE_BYTES
    allow_insecure_http: bool = False

    def __repr__(self) -> str:
        return (
            "AsyncDeviceClientConfig(base_url=<redacted>, api_key=<redacted>, "
            f"timeout={self.timeout!r}, retry={self.retry!r}, "
            f"max_response_bytes={self.max_response_bytes!r}, "
            f"allow_insecure_http={self.allow_insecure_http!r})"
        )


RequestOptionsInput: TypeAlias = RequestOptions | Mapping[str, object] | None


__all__ = [
    "AsyncCredentialProvider",
    "AsyncDeviceClientConfig",
    "AsyncSecretSource",
    "DeviceClientConfig",
    "RequestOptions",
    "RetryConfig",
    "SecretSource",
    "SyncCredentialProvider",
    "SyncSecretSource",
]
