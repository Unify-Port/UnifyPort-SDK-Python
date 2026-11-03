"""Public UnifyPort Device API SDK surface."""

from . import models as models
from ._generated import (
    NODE_OPERATION_IDS,
    OPERATIONS,
    PYTHON_METHODS,
    OperationSpec,
    ParameterSpec,
)
from .async_client import AsyncUnifyPortDeviceClient
from .client import UnifyPortDeviceClient
from .config import (
    AsyncCredentialProvider,
    AsyncDeviceClientConfig,
    AsyncSecretSource,
    DeviceClientConfig,
    RequestOptions,
    RetryConfig,
    SecretSource,
    SyncCredentialProvider,
    SyncSecretSource,
)
from .errors import (
    UnifyPortApiError,
    UnifyPortConfigurationError,
    UnifyPortError,
    UnifyPortNetworkError,
    UnifyPortPaginationError,
    UnifyPortResponseParseError,
    UnifyPortTimeoutError,
)
from .pagination import (
    CursorPage,
    CursorPaginationOptions,
    paginate_cursor,
    paginate_cursor_async,
)
from .result import ApiResult

# 分页响应与公开类型包含不兼容变化，使用新的 minor 版本承载迁移。
__version__ = "0.2.0"

# 根入口只显式列出稳定公共面；生成 model 通过 unifyport.models 模块访问。
__all__ = [
    "ApiResult",
    "AsyncCredentialProvider",
    "AsyncDeviceClientConfig",
    "AsyncSecretSource",
    "AsyncUnifyPortDeviceClient",
    "CursorPage",
    "CursorPaginationOptions",
    "DeviceClientConfig",
    "NODE_OPERATION_IDS",
    "OPERATIONS",
    "OperationSpec",
    "PYTHON_METHODS",
    "ParameterSpec",
    "RequestOptions",
    "RetryConfig",
    "SecretSource",
    "SyncCredentialProvider",
    "SyncSecretSource",
    "UnifyPortApiError",
    "UnifyPortConfigurationError",
    "UnifyPortDeviceClient",
    "UnifyPortError",
    "UnifyPortNetworkError",
    "UnifyPortPaginationError",
    "UnifyPortResponseParseError",
    "UnifyPortTimeoutError",
    "models",
    "paginate_cursor",
    "paginate_cursor_async",
]
