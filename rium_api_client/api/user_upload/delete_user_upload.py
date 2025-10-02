from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_user_upload_response_200 import DeleteUserUploadResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    user_upload_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/user-uploads/{user_upload_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteUserUploadResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DeleteUserUploadResponse200.from_dict(response.json())

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
) -> Response[Union[DeleteUserUploadResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_upload_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[DeleteUserUploadResponse200, ErrorResponse]]:
    """アップロードファイルの削除

     指定したアップロードファイルを削除する。

    Args:
        user_upload_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteUserUploadResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        user_upload_id=user_upload_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_upload_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DeleteUserUploadResponse200, ErrorResponse]]:
    """アップロードファイルの削除

     指定したアップロードファイルを削除する。

    Args:
        user_upload_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteUserUploadResponse200, ErrorResponse]
    """

    return sync_detailed(
        user_upload_id=user_upload_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_upload_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[DeleteUserUploadResponse200, ErrorResponse]]:
    """アップロードファイルの削除

     指定したアップロードファイルを削除する。

    Args:
        user_upload_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteUserUploadResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        user_upload_id=user_upload_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_upload_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DeleteUserUploadResponse200, ErrorResponse]]:
    """アップロードファイルの削除

     指定したアップロードファイルを削除する。

    Args:
        user_upload_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteUserUploadResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            user_upload_id=user_upload_id,
            client=client,
        )
    ).parsed
