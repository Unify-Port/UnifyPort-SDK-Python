"""Stable public errors that intentionally retain no raw transport objects."""

from __future__ import annotations


class UnifyPortError(Exception):
    """Base class for SDK failures."""

    __slots__ = ("operation_id",)

    def __init__(self, message: str, *, operation_id: str | None = None) -> None:
        super().__init__(message)
        self.operation_id = operation_id


class UnifyPortConfigurationError(UnifyPortError):
    """Raised when client or request configuration violates a safe boundary."""

    __slots__ = ("field", "reason")

    def __init__(self, field: str, reason: str) -> None:
        # 错误只包含稳定字段名与原因，避免把原始配置值带入日志。
        super().__init__(f"UnifyPort SDK configuration error: {field} {reason}")
        self.field = field
        self.reason = reason


class UnifyPortNetworkError(UnifyPortError):
    """Raised when no usable HTTP response can be obtained."""

    __slots__ = ()

    def __init__(self, *, operation_id: str | None = None) -> None:
        super().__init__(
            _operation_message("UnifyPort network request failed", operation_id),
            operation_id=operation_id,
        )


class UnifyPortTimeoutError(UnifyPortNetworkError):
    """Raised when the complete logical operation exceeds its deadline."""

    __slots__ = ("timeout",)

    def __init__(self, timeout: float, *, operation_id: str | None = None) -> None:
        UnifyPortError.__init__(
            self,
            _operation_message("UnifyPort request timed out", operation_id),
            operation_id=operation_id,
        )
        self.timeout = timeout


class UnifyPortResponseParseError(UnifyPortError):
    """Raised for oversized, unreadable, or invalid response bodies."""

    __slots__ = ("status", "request_id")

    def __init__(
        self,
        *,
        operation_id: str | None = None,
        status: int | None = None,
        request_id: str | None = None,
    ) -> None:
        # body、headers 与解析器异常都可能含敏感内容，公开对象只保留筛选后的诊断值。
        super().__init__(
            _operation_message("Unable to parse UnifyPort API response", operation_id),
            operation_id=operation_id,
        )
        self.status = status
        self.request_id = request_id


class UnifyPortApiError(UnifyPortError):
    """Raised for non-success HTTP responses."""

    __slots__ = ("status", "code", "numeric_code", "request_id", "details")

    def __init__(
        self,
        *,
        status: int,
        code: str,
        operation_id: str | None = None,
        request_id: str | None = None,
        numeric_code: str | None = None,
    ) -> None:
        message = f"UnifyPort API returned {code} (HTTP {status})"
        super().__init__(_operation_message(message, operation_id), operation_id=operation_id)
        self.status = status
        self.code = code
        # 可选字段保持旧构造调用兼容，不让原始错误文本进入公开对象。
        self.numeric_code = numeric_code
        self.request_id = request_id
        # 上游 details 常回显输入，保留属性兼容性但永远不保留原值。
        self.details: None = None


class UnifyPortPaginationError(UnifyPortError):
    """Raised when cursor pagination cannot terminate safely."""

    __slots__ = ()


def _operation_message(message: str, operation_id: str | None) -> str:
    return message if operation_id is None else f"{message} ({operation_id})"


__all__ = [
    "UnifyPortApiError",
    "UnifyPortConfigurationError",
    "UnifyPortError",
    "UnifyPortNetworkError",
    "UnifyPortPaginationError",
    "UnifyPortResponseParseError",
    "UnifyPortTimeoutError",
]
