# Changelog

All notable SDK changes are documented here. The format follows Keep a Changelog, and the project uses
Semantic Versioning for the Python distribution.

## 0.2.0 - prepared, unreleased

### Added

- Synchronizes 78 HTTP operations and 225 schemas; adds Facebook session/E2EE direct-message types and four receiver declarations with eight examples.
- Provides 40 receiver declarations and 57 synthetic examples covering 29 declarations; retains 24 standard event names plus `*`.
- Adds optional filtered numeric error metadata; retry and credential boundaries remain unchanged.

### Changed

- Account pagination, separate creation/update schemas, asynchronous deletion, optional wallet/QR fields and corrected message/Webhook unions require consumer migration from 0.1.0.

### Fixed

- Preserves quoted and unquoted RFC3339 nanosecond timestamps in generated fixtures and type cases with an isolated SafeLoader, including timezone offsets and trailing zeros.

See [release notes](docs/release-notes.md), [migration guide](docs/migration.md), [简体中文发布说明](docs/zh-CN/release-notes.md) and [简体中文迁移指南](docs/zh-CN/migration.md). No tag or PyPI publication has been performed.

## [0.1.0] - 2026-07-31

### Added

- Initial synchronous and asynchronous Device API clients.
- Generated coverage for the Node SDK `v0.4.0` public surface: 64 operations and 70 schemas.
- Security-oriented transport, error, retry, timeout, response-size, and pagination behavior.
- Deterministic generation, parity, packaging, public artifact, and bilingual documentation gates.

[0.1.0]: https://github.com/Unify-Port/UnifyPort-SDK-Python/releases/tag/v0.1.0
