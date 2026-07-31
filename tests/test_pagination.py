from __future__ import annotations

import asyncio

import pytest

from unifyport import (
    CursorPage,
    UnifyPortPaginationError,
    paginate_cursor,
    paginate_cursor_async,
)


def test_sync_cursor_pagination_is_finite_and_ordered() -> None:
    cursors: list[str | None] = []

    def fetch_page(cursor: str | None) -> CursorPage[int]:
        cursors.append(cursor)
        if cursor is None:
            return CursorPage(items=(1, 2), has_more=True, next_cursor="next")
        return CursorPage(items=(3,), has_more=False)

    assert list(paginate_cursor(fetch_page, max_pages=2)) == [1, 2, 3]
    assert cursors == [None, "next"]


@pytest.mark.parametrize(
    ("fetch_page", "message"),
    [
        (lambda _cursor: {"items": [], "has_more": True}, "without next_cursor"),
        (
            lambda _cursor: {"items": [], "has_more": True, "next_cursor": "same"},
            "repeated next_cursor",
        ),
    ],
)
def test_cursor_pagination_rejects_broken_cursor_chains(
    fetch_page: object,
    message: str,
) -> None:
    # callback 类型在参数化后被擦除；运行时仍应给出稳定 pagination error。
    callback = fetch_page
    with pytest.raises(UnifyPortPaginationError, match=message):
        list(paginate_cursor(callback, initial_cursor="same"))  # type: ignore[arg-type]


def test_cursor_pagination_enforces_max_pages_without_echoing_cursor() -> None:
    cursor = "sensitive-cursor"

    with pytest.raises(UnifyPortPaginationError, match="max_pages=1") as captured:
        list(
            paginate_cursor(
                lambda _cursor: CursorPage(
                    items=(),
                    has_more=True,
                    next_cursor=cursor,
                ),
                max_pages=1,
            )
        )

    assert cursor not in str(captured.value)


async def test_async_cursor_pagination_matches_sync_semantics() -> None:
    calls = 0

    async def fetch_page(cursor: str | None) -> CursorPage[str]:
        nonlocal calls
        calls += 1
        await asyncio.sleep(0)
        if cursor is None:
            return CursorPage(items=("a",), has_more=True, next_cursor="next")
        return CursorPage(items=("b",), has_more=False)

    values = [item async for item in paginate_cursor_async(fetch_page, max_pages=2)]

    assert values == ["a", "b"]
    assert calls == 2
