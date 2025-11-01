import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.event_list_response import EventListResponse
from ...models.get_events_direction import GetEventsDirection
from ...models.get_events_sort import GetEventsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: Union[Unset, datetime.date] = UNSET,
    end: Union[Unset, datetime.date] = UNSET,
    loggable_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    taxon_id: Union[Unset, int] = UNSET,
    genre_id: Union[Unset, int] = UNSET,
    tag_ids: Union[Unset, list[int]] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetEventsSort] = GetEventsSort.TIME,
    direction: Union[Unset, GetEventsDirection] = GetEventsDirection.DESC,
    str_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start: Union[Unset, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    json_end: Union[Unset, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    params["loggable_id"] = loggable_id

    json_user_id: Union[Unset, str] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["user_id"] = json_user_id

    params["taxon_id"] = taxon_id

    params["genre_id"] = genre_id

    json_tag_ids: Union[Unset, list[int]] = UNSET
    if not isinstance(tag_ids, Unset):
        json_tag_ids = tag_ids

    params["tag_ids"] = json_tag_ids

    params["fields"] = fields

    params["limit"] = limit

    params["page"] = page

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_direction: Union[Unset, str] = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    params["str"] = str_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, EventListResponse]]:
    if response.status_code == 200:
        response_200 = EventListResponse.from_dict(response.json())

        return response_200

    if 400 <= response.status_code <= 499:
        response_4xx = ErrorResponse.from_dict(response.json())

        return response_4xx

    if 500 <= response.status_code <= 599:
        response_5xx = ErrorResponse.from_dict(response.json())

        return response_5xx

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, EventListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.date] = UNSET,
    end: Union[Unset, datetime.date] = UNSET,
    loggable_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    taxon_id: Union[Unset, int] = UNSET,
    genre_id: Union[Unset, int] = UNSET,
    tag_ids: Union[Unset, list[int]] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetEventsSort] = GetEventsSort.TIME,
    direction: Union[Unset, GetEventsDirection] = GetEventsDirection.DESC,
    str_: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, EventListResponse]]:
    """飼育記録の一覧表示

     指定した条件に合致する飼育記録の一覧を取得する。

    Args:
        start (Union[Unset, datetime.date]):
        end (Union[Unset, datetime.date]):
        loggable_id (Union[Unset, int]):
        user_id (Union[Unset, UUID]):
        taxon_id (Union[Unset, int]):
        genre_id (Union[Unset, int]):
        tag_ids (Union[Unset, list[int]]):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetEventsSort]):  Default: GetEventsSort.TIME.
        direction (Union[Unset, GetEventsDirection]):  Default: GetEventsDirection.DESC.
        str_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, EventListResponse]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        loggable_id=loggable_id,
        user_id=user_id,
        taxon_id=taxon_id,
        genre_id=genre_id,
        tag_ids=tag_ids,
        fields=fields,
        limit=limit,
        page=page,
        sort=sort,
        direction=direction,
        str_=str_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.date] = UNSET,
    end: Union[Unset, datetime.date] = UNSET,
    loggable_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    taxon_id: Union[Unset, int] = UNSET,
    genre_id: Union[Unset, int] = UNSET,
    tag_ids: Union[Unset, list[int]] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetEventsSort] = GetEventsSort.TIME,
    direction: Union[Unset, GetEventsDirection] = GetEventsDirection.DESC,
    str_: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, EventListResponse]]:
    """飼育記録の一覧表示

     指定した条件に合致する飼育記録の一覧を取得する。

    Args:
        start (Union[Unset, datetime.date]):
        end (Union[Unset, datetime.date]):
        loggable_id (Union[Unset, int]):
        user_id (Union[Unset, UUID]):
        taxon_id (Union[Unset, int]):
        genre_id (Union[Unset, int]):
        tag_ids (Union[Unset, list[int]]):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetEventsSort]):  Default: GetEventsSort.TIME.
        direction (Union[Unset, GetEventsDirection]):  Default: GetEventsDirection.DESC.
        str_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, EventListResponse]
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
        loggable_id=loggable_id,
        user_id=user_id,
        taxon_id=taxon_id,
        genre_id=genre_id,
        tag_ids=tag_ids,
        fields=fields,
        limit=limit,
        page=page,
        sort=sort,
        direction=direction,
        str_=str_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.date] = UNSET,
    end: Union[Unset, datetime.date] = UNSET,
    loggable_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    taxon_id: Union[Unset, int] = UNSET,
    genre_id: Union[Unset, int] = UNSET,
    tag_ids: Union[Unset, list[int]] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetEventsSort] = GetEventsSort.TIME,
    direction: Union[Unset, GetEventsDirection] = GetEventsDirection.DESC,
    str_: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, EventListResponse]]:
    """飼育記録の一覧表示

     指定した条件に合致する飼育記録の一覧を取得する。

    Args:
        start (Union[Unset, datetime.date]):
        end (Union[Unset, datetime.date]):
        loggable_id (Union[Unset, int]):
        user_id (Union[Unset, UUID]):
        taxon_id (Union[Unset, int]):
        genre_id (Union[Unset, int]):
        tag_ids (Union[Unset, list[int]]):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetEventsSort]):  Default: GetEventsSort.TIME.
        direction (Union[Unset, GetEventsDirection]):  Default: GetEventsDirection.DESC.
        str_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, EventListResponse]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        loggable_id=loggable_id,
        user_id=user_id,
        taxon_id=taxon_id,
        genre_id=genre_id,
        tag_ids=tag_ids,
        fields=fields,
        limit=limit,
        page=page,
        sort=sort,
        direction=direction,
        str_=str_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.date] = UNSET,
    end: Union[Unset, datetime.date] = UNSET,
    loggable_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    taxon_id: Union[Unset, int] = UNSET,
    genre_id: Union[Unset, int] = UNSET,
    tag_ids: Union[Unset, list[int]] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetEventsSort] = GetEventsSort.TIME,
    direction: Union[Unset, GetEventsDirection] = GetEventsDirection.DESC,
    str_: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, EventListResponse]]:
    """飼育記録の一覧表示

     指定した条件に合致する飼育記録の一覧を取得する。

    Args:
        start (Union[Unset, datetime.date]):
        end (Union[Unset, datetime.date]):
        loggable_id (Union[Unset, int]):
        user_id (Union[Unset, UUID]):
        taxon_id (Union[Unset, int]):
        genre_id (Union[Unset, int]):
        tag_ids (Union[Unset, list[int]]):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetEventsSort]):  Default: GetEventsSort.TIME.
        direction (Union[Unset, GetEventsDirection]):  Default: GetEventsDirection.DESC.
        str_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, EventListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
            loggable_id=loggable_id,
            user_id=user_id,
            taxon_id=taxon_id,
            genre_id=genre_id,
            tag_ids=tag_ids,
            fields=fields,
            limit=limit,
            page=page,
            sort=sort,
            direction=direction,
            str_=str_,
        )
    ).parsed
