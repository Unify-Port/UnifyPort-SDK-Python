# UnifyPort Python SDK

[English](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/README.md) |
[简体中文](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/README.zh-CN.md) |
[Website](https://www.unifyport.ai)

Type-safe sync and async Python clients for the public UnifyPort Device API. The SDK is generated from
the approved public OpenAPI contract and currently tracks `@unifyport/sdk-node` `v0.4.0`: 78 operations,
218 component schemas, and the same retry and secret-handling classifications.

The Python package is `unifyport-sdk`; the import package is `unifyport`. This repository starts at SDK
version `0.1.0`. A Git tag or local build alone does not prove that a version reached PyPI.

## Requirements

- Python `>=3.11`
- `httpx` `>=0.27,<1`
- `typing-extensions` `>=4.13,<5` for the Python 3.11-3.13 PEP 728 backport

Install the published package from PyPI:

```bash
python -m pip install unifyport-sdk
```

To work from a source checkout:

```bash
python -m pip install -e ".[dev]"
```

## Quick start

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

The async client exposes the same generated snake_case operation surface:

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

Generated operation methods expose path, query, and the allowlisted `x_request_id` header as typed keyword
arguments, plus typed `body=` and `options=` when applicable. Authentication is never an operation argument:

```python
account = device.get_account(account_id="acc_example", x_request_id="req_example")
```

Every call returns `ApiResult[data]` with only filtered metadata: `data`, `status`, and optional
`request_id`. Raw `httpx.Response` objects are intentionally not public.

## Safety boundaries

- `X-Api-Key` comes only from client configuration and is resolved once per logical operation.
- HTTPS is required by default. Explicitly enabled plaintext HTTP remains limited to loopback hosts.
- Redirects are not followed, and credential-bearing requests cannot escape the configured origin or
  base path.
- Automatic retry is restricted to the 19 reviewed operations and the statuses `408`, `429`, `502`,
  `503`, and `504`, plus transport failures. Per-call settings can only tighten the global budget.
- Requests require identity encoding; compressed responses are rejected before raw bodies are streamed
  through the byte limit and parsed as JSON.
- Public errors retain stable status, error code, operation ID, and request ID only; raw response text,
  query strings, credentials, and underlying exception text are not exposed.
- Cursor helpers enforce a finite page limit and reject missing or repeated cursors.
- `provider_profile` and `reply_token` are sensitive outputs. Do not log complete account or message
  responses.

The package does not expose MCP tools, Agent Skills, a generic raw-request escape hatch, provider-specific
orchestration, or an inferred webhook-signature algorithm.

## Contract and generated code

`contracts/device.openapi.yaml` is the only protocol source for generation. The language-neutral policy
file records semantics that cannot be inferred safely from HTTP methods. Do not edit
`src/unifyport/_generated/` or generated API reference pages directly.

```bash
python scripts/generate.py
python scripts/generate.py --check
python scripts/check_node_parity.py --node-repo ../UnifyPort-SDK-Nodejs --node-ref 5901244c409f63fd6b77a899c239ebc9ee96dd50
```

See the [API coverage report](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/docs/api-coverage.md),
[architecture](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/docs/architecture.md),
[security boundaries](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/docs/security.md),
[contract maintenance guide](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/docs/contract-maintenance.md),
[acceptance report](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/docs/acceptance-report.md),
and [release notes](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/docs/release-notes.md).

## Validation

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

The SDK source is available under the
[MIT License](https://github.com/Unify-Port/UnifyPort-SDK-Python/blob/main/LICENSE). The Device API
contract describes the service interface and retains its own license metadata.

The synchronization baseline is approved Node source `5901244`, not a claim that npm has released these capabilities. No package is published by this update. See [Contract update](docs/contract-update.md).
