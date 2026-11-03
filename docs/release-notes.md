# Release notes

[English](release-notes.md) | [简体中文](zh-CN/release-notes.md)

## Unreleased - Facebook

Adds the facebook provider and four typed standard receiver declarations. Includes sparse media and session-only authorization coverage. HTTP methods, event names and retry policy remain unchanged; provider switches may require a new branch. See the Facebook channel guide. No publication or deployment is implied.

## Unreleased

Synchronize 78 HTTP operations, 218 schemas, numeric error metadata and Webhook types. The package version is unchanged; see [Contract update](contract-update.md).

## 0.1.0

Initial Python SDK implementation for the public UnifyPort Device API:

- Sync and async HTTPX clients with 64 generated snake_case operation methods.
- 70 generated schema types based on the Node SDK `v0.4.0` public contract.
- Typed, open `ProviderProfile` standard fields and optional `SendMessageResult.reply_token` support.
- Deterministic generation, Node parity manifest, bilingual operation reference, and public artifact gate.
- HTTPS/base-path confinement, credential isolation, allowlisted retries, total deadlines, bounded response
  streaming, sanitized errors, and finite cursor pagination.

The Python version is independent from the Node SDK version. Registry publication and real-provider E2E
are separate release actions and are not asserted by these notes.
