# Security boundaries

[English](security.md) | [简体中文](zh-CN/security.md)

## Credentials

- The Device API uses `X-Api-Key`. It can be supplied only when constructing a client.
- A string or credential provider is resolved once per logical operation. Retries reuse that resolved
  value and never persist it in public result or error objects.
- Operation headers are allowlisted separately. `Authorization`, `Cookie`, and `X-Api-Key` cannot be
  injected through a generated method.
- Configuration representations redact both the API key and base URL.

## Request confinement

- HTTPS is mandatory unless `allow_insecure_http=True` and the host is loopback.
- Base URLs containing user information, query strings, or fragments are rejected.
- Every final request must stay on the configured origin and under its configured base path.
- Redirect following is disabled. A redirect response is handled as a non-success API response.
- `transport=` is a trusted dependency-injection point for tests or controlled integrations. It receives
  the complete request, including `X-Api-Key`, and can perform its own I/O. Origin, base-path, proxy, and
  redirect protections constrain the request produced by the SDK; they cannot constrain arbitrary code
  inside a custom transport. Never accept a transport from an untrusted source.

## Retry and timeout

Only the 19 operations in the policy allowlist can retry. Retry candidates are transport failures and
HTTP `408`, `429`, `502`, `503`, and `504`. Backoff uses full jitter; valid `Retry-After` values are
honored only within the configured delay cap. A single operation may disable or reduce retries, never
grant retries to a different operation.

The configured timeout is a total logical deadline across credential resolution, attempts, response
streaming, and backoff. Per-call timeouts can only reduce that deadline. Cooperative HTTP work and
async credential providers are cancelled at the deadline. Python cannot safely pre-empt an arbitrary
blocking sync credential callback or custom transport; if one returns after the deadline, the SDK
reports a timeout and does not start a later request with the expired credential. External async task
cancellation remains native `asyncio.CancelledError` control flow.

## Responses and errors

- Requests force `Accept-Encoding: identity`. A response with any non-identity `Content-Encoding` is
  rejected before its body is read, so an HTTP client cannot transparently inflate a compressed chunk
  outside the configured byte budget.
- Response bodies are streamed through an 8 MiB default limit; configuration cannot exceed 64 MiB.
- Invalid or oversized response content raises `UnifyPortResponseParseError` without retaining content.
- API errors expose only validated `status`, a bounded diagnostic `code`, and a bounded request ID.
- Transport exception text, raw responses, headers, bodies, URLs with query strings, and server-provided
  messages/details do not enter public errors.
- `ApiResult` carries `data`, `status`, and optional `request_id`; it has no raw response handle.

## Sensitive contract fields

The 12 `secretOutput` operations must be treated as sensitive. In particular, account responses can
contain `provider_profile`, and `send_message` can contain an optional opaque `reply_token`. The eight
`secretInput` operations cover credentials, sessions, endpoint secrets, and reusable reply capability.
Do not log, snapshot, or forward complete inputs or outputs for these operations.

## Explicitly absent capabilities

The package has no MCP exposure, generic raw request, provider-specific orchestration, webhook signing
guess, analytics identifier propagation, or credential logging hook. Additions in these areas require a
separate public contract and security review.
