"""Finite cursor pagination helpers for synchronous and asynchronous clients."""

from __future__ import annotations

import inspect
from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Mapping, Sequence
from dataclasses import dataclass
from typing import Generic, TypeAlias, TypeVar, cast

from .errors import UnifyPortPaginationError

T = TypeVar("T")

DEFAULT_MAX_PAGES = 10_000


@dataclass(frozen=True, slots=True)
class CursorPage(Generic[T]):
    """One decoded cursor page."""

    items: Sequence[T]
    has_more: bool
    next_cursor: str | None = None


@dataclass(frozen=True, slots=True)
class CursorPaginationOptions:
    """Finite bounds for a cursor traversal."""

    initial_cursor: str | None = None
    max_pages: int = DEFAULT_MAX_PAGES


PageMapping: TypeAlias = Mapping[str, object]
SyncPageFetcher: TypeAlias = Callable[[str | None], CursorPage[T] | PageMapping]
AsyncPageFetcher: TypeAlias = Callable[
    [str | None], CursorPage[T] | PageMapping | Awaitable[CursorPage[T] | PageMapping]
]


def paginate_cursor(
    fetch_page: SyncPageFetcher[T],
    options: CursorPaginationOptions | None = None,
    *,
    initial_cursor: str | None = None,
    max_pages: int | None = None,
) -> Iterator[T]:
    """Yield items page by page while rejecting non-terminating cursor chains."""

    settings = _pagination_options(options, initial_cursor=initial_cursor, max_pages=max_pages)
    cursor = settings.initial_cursor
    seen = set() if cursor is None else {cursor}
    for _page_number in range(settings.max_pages):
        page = _coerce_page(fetch_page(cursor))
        yield from page.items
        if not page.has_more:
            return
        cursor = _next_cursor(page, seen)
    raise UnifyPortPaginationError(f"cursor pagination exceeded max_pages={settings.max_pages}")


async def paginate_cursor_async(
    fetch_page: AsyncPageFetcher[T],
    options: CursorPaginationOptions | None = None,
    *,
    initial_cursor: str | None = None,
    max_pages: int | None = None,
) -> AsyncIterator[T]:
    """Asynchronous counterpart of :func:`paginate_cursor`."""

    settings = _pagination_options(options, initial_cursor=initial_cursor, max_pages=max_pages)
    cursor = settings.initial_cursor
    seen = set() if cursor is None else {cursor}
    for _page_number in range(settings.max_pages):
        candidate = fetch_page(cursor)
        if inspect.isawaitable(candidate):
            candidate = await candidate
        page = _coerce_page(candidate)
        for item in page.items:
            yield item
        if not page.has_more:
            return
        cursor = _next_cursor(page, seen)
    raise UnifyPortPaginationError(f"cursor pagination exceeded max_pages={settings.max_pages}")


def _pagination_options(
    options: CursorPaginationOptions | None,
    *,
    initial_cursor: str | None,
    max_pages: int | None,
) -> CursorPaginationOptions:
    if options is not None and (initial_cursor is not None or max_pages is not None):
        raise UnifyPortPaginationError(
            "pagination options cannot be combined with keyword overrides"
        )
    settings = options or CursorPaginationOptions(
        initial_cursor=initial_cursor,
        max_pages=DEFAULT_MAX_PAGES if max_pages is None else max_pages,
    )
    if not isinstance(settings, CursorPaginationOptions):
        raise UnifyPortPaginationError("options must be CursorPaginationOptions")
    if (
        not isinstance(settings.max_pages, int)
        or isinstance(settings.max_pages, bool)
        or settings.max_pages <= 0
    ):
        raise UnifyPortPaginationError("max_pages must be a positive integer")
    if settings.initial_cursor is not None and (
        not isinstance(settings.initial_cursor, str) or not settings.initial_cursor
    ):
        raise UnifyPortPaginationError("initial_cursor must be a non-empty string")
    return settings


def _coerce_page(value: CursorPage[T] | PageMapping) -> CursorPage[T]:
    if isinstance(value, CursorPage):
        page = value
    elif isinstance(value, Mapping):
        items = value.get("items")
        has_more = value.get("has_more")
        next_cursor = value.get("next_cursor")
        if not isinstance(items, Sequence) or isinstance(items, (str, bytes, bytearray)):
            raise UnifyPortPaginationError("cursor page items must be a sequence")
        if not isinstance(has_more, bool):
            raise UnifyPortPaginationError("cursor page has_more must be a boolean")
        if next_cursor is not None and not isinstance(next_cursor, str):
            raise UnifyPortPaginationError("cursor page next_cursor must be a string")
        # 复制 items，避免 callback 在逐项 yield 时并发修改同一页。
        page = CursorPage(
            items=tuple(cast(Sequence[T], items)),
            has_more=has_more,
            next_cursor=next_cursor,
        )
    else:
        raise UnifyPortPaginationError("fetch_page returned an invalid cursor page")
    if not isinstance(page.items, Sequence) or isinstance(page.items, (str, bytes, bytearray)):
        raise UnifyPortPaginationError("cursor page items must be a sequence")
    if not isinstance(page.has_more, bool):
        raise UnifyPortPaginationError("cursor page has_more must be a boolean")
    if page.next_cursor is not None and not isinstance(page.next_cursor, str):
        raise UnifyPortPaginationError("cursor page next_cursor must be a string")
    return page


def _next_cursor(page: CursorPage[T], seen: set[str]) -> str:
    cursor = page.next_cursor
    if cursor is None or cursor == "":
        raise UnifyPortPaginationError("upstream returned has_more=true without next_cursor")
    if cursor in seen:
        # cursor 可能是敏感定位值，错误只说明重复而不回显具体内容。
        raise UnifyPortPaginationError("upstream returned a repeated next_cursor")
    seen.add(cursor)
    return cursor


__all__ = [
    "CursorPage",
    "CursorPaginationOptions",
    "paginate_cursor",
    "paginate_cursor_async",
]
