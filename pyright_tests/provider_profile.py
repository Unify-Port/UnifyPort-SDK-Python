"""Pyright-only assertions for the open ProviderProfile contract."""

from typing import assert_type

from unifyport import models

# ProviderProfile 必须保留 provider-specific JSON，同时不放宽已知字段的精确类型。
profile: models.ProviderProfile = {
    "id": "provider-user-id",
    "provider_specific": {"verified": True},
}

assert_type(profile["id"], str)
assert_type(profile["provider_specific"], models.JsonValue)
