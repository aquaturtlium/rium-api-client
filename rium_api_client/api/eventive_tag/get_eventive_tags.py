from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.eventive_tag_list_response import EventiveTagListResponse
from ...models.get_eventive_tags_direction import GetEventiveTagsDirection
from ...models.get_eventive_tags_sort import GetEventiveTagsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    includes: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetEventiveTagsSort] = GetEventiveTagsSort.NAME,
    direction: Union[Unset, GetEventiveTagsDirection] = GetEventiveTagsDirection.ASC,
    str_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["includes"] = includes

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
        "url": "/eventive-tags",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, EventiveTagListResponse]]:
    if response.status_code == 200:
        response_200 = EventiveTagListResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, EventiveTagListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    includes: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetEventiveTagsSort] = GetEventiveTagsSort.NAME,
    direction: Union[Unset, GetEventiveTagsDirection] = GetEventiveTagsDirection.ASC,
    str_: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, EventiveTagListResponse]]:
    """飼育記録タグの一覧表示

     指定した条件に合致する飼育記録タグの一覧を取得する。

    Args:
        includes (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetEventiveTagsSort]):  Default: GetEventiveTagsSort.NAME.
        direction (Union[Unset, GetEventiveTagsDirection]):  Default:
            GetEventiveTagsDirection.ASC.
        str_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, EventiveTagListResponse]]
    """

    kwargs = _get_kwargs(
        includes=includes,
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
    includes: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetEventiveTagsSort] = GetEventiveTagsSort.NAME,
    direction: Union[Unset, GetEventiveTagsDirection] = GetEventiveTagsDirection.ASC,
    str_: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, EventiveTagListResponse]]:
    """飼育記録タグの一覧表示

     指定した条件に合致する飼育記録タグの一覧を取得する。

    Args:
        includes (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetEventiveTagsSort]):  Default: GetEventiveTagsSort.NAME.
        direction (Union[Unset, GetEventiveTagsDirection]):  Default:
            GetEventiveTagsDirection.ASC.
        str_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, EventiveTagListResponse]
    """

    return sync_detailed(
        client=client,
        includes=includes,
        limit=limit,
        page=page,
        sort=sort,
        direction=direction,
        str_=str_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    includes: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetEventiveTagsSort] = GetEventiveTagsSort.NAME,
    direction: Union[Unset, GetEventiveTagsDirection] = GetEventiveTagsDirection.ASC,
    str_: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, EventiveTagListResponse]]:
    """飼育記録タグの一覧表示

     指定した条件に合致する飼育記録タグの一覧を取得する。

    Args:
        includes (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetEventiveTagsSort]):  Default: GetEventiveTagsSort.NAME.
        direction (Union[Unset, GetEventiveTagsDirection]):  Default:
            GetEventiveTagsDirection.ASC.
        str_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, EventiveTagListResponse]]
    """

    kwargs = _get_kwargs(
        includes=includes,
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
    includes: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetEventiveTagsSort] = GetEventiveTagsSort.NAME,
    direction: Union[Unset, GetEventiveTagsDirection] = GetEventiveTagsDirection.ASC,
    str_: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, EventiveTagListResponse]]:
    """飼育記録タグの一覧表示

     指定した条件に合致する飼育記録タグの一覧を取得する。

    Args:
        includes (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetEventiveTagsSort]):  Default: GetEventiveTagsSort.NAME.
        direction (Union[Unset, GetEventiveTagsDirection]):  Default:
            GetEventiveTagsDirection.ASC.
        str_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, EventiveTagListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            includes=includes,
            limit=limit,
            page=page,
            sort=sort,
            direction=direction,
            str_=str_,
        )
    ).parsed
