from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.event_response import EventResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_id: int,
    *,
    includes: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["includes"] = includes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/events/{event_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, EventResponse]]:
    if response.status_code == 200:
        response_200 = EventResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, EventResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_id: int,
    *,
    client: AuthenticatedClient,
    includes: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, EventResponse]]:
    """飼育記録の詳細表示

     指定した飼育記録の詳細を取得する。

    Args:
        event_id (int):
        includes (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, EventResponse]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        includes=includes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: int,
    *,
    client: AuthenticatedClient,
    includes: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, EventResponse]]:
    """飼育記録の詳細表示

     指定した飼育記録の詳細を取得する。

    Args:
        event_id (int):
        includes (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, EventResponse]
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        includes=includes,
    ).parsed


async def asyncio_detailed(
    event_id: int,
    *,
    client: AuthenticatedClient,
    includes: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, EventResponse]]:
    """飼育記録の詳細表示

     指定した飼育記録の詳細を取得する。

    Args:
        event_id (int):
        includes (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, EventResponse]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        includes=includes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: int,
    *,
    client: AuthenticatedClient,
    includes: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, EventResponse]]:
    """飼育記録の詳細表示

     指定した飼育記録の詳細を取得する。

    Args:
        event_id (int):
        includes (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, EventResponse]
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            includes=includes,
        )
    ).parsed
