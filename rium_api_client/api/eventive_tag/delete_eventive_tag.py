from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_eventive_tag_response_200 import DeleteEventiveTagResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    eventive_tag_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/eventive-tags/{eventive_tag_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteEventiveTagResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DeleteEventiveTagResponse200.from_dict(response.json())

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
) -> Response[Union[DeleteEventiveTagResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    eventive_tag_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[DeleteEventiveTagResponse200, ErrorResponse]]:
    """飼育記録タグの削除

     指定した飼育記録タグを削除する。

    Args:
        eventive_tag_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteEventiveTagResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        eventive_tag_id=eventive_tag_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    eventive_tag_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DeleteEventiveTagResponse200, ErrorResponse]]:
    """飼育記録タグの削除

     指定した飼育記録タグを削除する。

    Args:
        eventive_tag_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteEventiveTagResponse200, ErrorResponse]
    """

    return sync_detailed(
        eventive_tag_id=eventive_tag_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    eventive_tag_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[DeleteEventiveTagResponse200, ErrorResponse]]:
    """飼育記録タグの削除

     指定した飼育記録タグを削除する。

    Args:
        eventive_tag_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteEventiveTagResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        eventive_tag_id=eventive_tag_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    eventive_tag_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DeleteEventiveTagResponse200, ErrorResponse]]:
    """飼育記録タグの削除

     指定した飼育記録タグを削除する。

    Args:
        eventive_tag_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteEventiveTagResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            eventive_tag_id=eventive_tag_id,
            client=client,
        )
    ).parsed
