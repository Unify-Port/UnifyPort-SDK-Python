# UnifyPort Python SDK

[English](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/README.md) |
[简体中文](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/README.zh-CN.md) |
[官网](https://www.unifyport.ai)

面向公开 UnifyPort Device API 的类型化同步与异步 Python client。SDK 根据已批准的公开 OpenAPI
contract 生成，当前对齐已批准的公开 Node 源码 `ce60499`：78 个 operation、225 个 component schema，
以及相同的 retry 和 secret 分类。

Python distribution 名为 `unifyport-sdk`，import package 为 `unifyport`。本仓库从 SDK `0.1.0`
开始；仅有 Git tag 或本地 build 不能证明该版本已进入 PyPI。

## 环境要求

- Python `>=3.11`
- `httpx` `>=0.27,<1`
- `typing-extensions` `>=4.13,<5`，用于 Python 3.11-3.13 的 PEP 728 backport

从 PyPI 安装已发布版本：

```bash
python -m pip install unifyport-sdk
```

从源码 checkout 开发安装：

```bash
python -m pip install -e ".[dev]"
```

## 快速开始

```python
import os

from unifyport import UnifyPortDeviceClient


def required_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


with UnifyPortDeviceClient(
    base_url=required_env("UNIFYPORT_DEVICE_API_BASE_URL"),
    api_key=required_env("UNIFYPORT_DEVICE_API_KEY"),
) as device:
    workspace = device.get_workspace()
    print(workspace.data)
```

异步 client 提供完全相同的 snake_case operation surface：

```python
import os

from unifyport import AsyncUnifyPortDeviceClient


async def main() -> None:
    async with AsyncUnifyPortDeviceClient(
        base_url=os.environ["UNIFYPORT_DEVICE_API_BASE_URL"],
        api_key=os.environ["UNIFYPORT_DEVICE_API_KEY"],
    ) as device:
        workspace = await device.get_workspace()
        print(workspace.data)
```

生成的 operation method 会将 path、query 与 allowlist 中的 `x_request_id` header 展开为类型化 keyword
参数，并按需提供类型化 `body=` 和 `options=`。认证信息永远不是 operation 参数：

```python
account = device.get_account(account_id="acc_example", x_request_id="req_example")
```

每次调用返回 `ApiResult[data]`，只包含经过筛选的 `data`、`status` 和可选 `request_id`；SDK
有意不公开 raw `httpx.Response`。

## 安全边界

- `X-Api-Key` 只能来自 client config，每个 logical operation 只解析一次。
- 默认必须使用 HTTPS；即使显式启用明文 HTTP，也仅允许 loopback host。
- 不跟随 redirect，携带 credential 的请求不能逃逸配置的 origin 或 base path。
- 自动 retry 仅限 19 个已审查 operation，以及 `408`、`429`、`502`、`503`、`504` 和网络失败；
  单次配置只能收紧全局预算。
- request 强制使用 identity encoding；compressed response 会在读取前被拒绝，raw body 随后才经过
  streaming byte limit 与 JSON 解析。
- 公开错误只保留稳定的 status、error code、operation ID 和 request ID，不暴露 response text、query、
  credential 或底层异常文本。
- cursor helper 有有限页数上限，并拒绝缺失或重复 cursor。
- `provider_profile` 和 `reply_token` 属于敏感输出，不要记录完整账号或消息响应。

本 package 不提供 MCP、Agent Skills、通用 raw-request 逃生口、provider-specific orchestration，也不推断
未公开的 webhook 签名算法。

## Contract 与生成代码

`contracts/device.openapi.yaml` 是唯一协议生成来源。language-neutral policy 文件保存无法从 HTTP method
安全推导的语义。不要直接修改 `src/unifyport/_generated/` 或生成的 API reference 页面。

```bash
python scripts/generate.py
python scripts/generate.py --check
python scripts/check_node_parity.py --node-repo ../UnifyPort-SDK-Nodejs --node-ref ce60499d7169c860ed3f64a686e04bff44316f35
```

更多信息见
[API coverage](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/docs/api-coverage.md)、
[架构](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/docs/zh-CN/architecture.md)、
[安全边界](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/docs/zh-CN/security.md)、
[contract 维护](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/docs/zh-CN/contract-maintenance.md)、
[验收报告](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/docs/zh-CN/acceptance-report.md) 和
[release notes](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/docs/zh-CN/release-notes.md)。

## 验收命令

```bash
ruff format --check .
ruff check .
mypy --strict src scripts typing_tests
npx --yes pyright@1.1.411 pyright_tests
pytest
python -m build
twine check dist/*
python scripts/check_public.py dist/*
python scripts/smoke_installed.py
pip-audit
```

## License

SDK source 使用
[MIT License](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/LICENSE)。Device API contract
描述服务接口，并保留自身 license metadata。

当前同步基线是已批准的 Node 源码 `ce60499`，不代表 npm 已发布同等能力。本轮未发布任何包。详见 [本次契约更新](docs/zh-CN/contract-update.md)。

[Facebook 渠道支持](docs/zh-CN/facebook.md)说明 session 授权、消息能力和标准回调。
