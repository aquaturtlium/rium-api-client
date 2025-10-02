from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.user_upload_post_request import UserUploadPostRequest
from ...models.user_upload_response import UserUploadResponse
from ...types import Response


def _get_kwargs(
    *,
    body: UserUploadPostRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/user-uploads",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UserUploadResponse]]:
    if response.status_code == 201:
        response_201 = UserUploadResponse.from_dict(response.json())

        return response_201

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
) -> Response[Union[ErrorResponse, UserUploadResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UserUploadPostRequest,
) -> Response[Union[ErrorResponse, UserUploadResponse]]:
    """アップロードファイルの作成

     新しいアップロードファイルを作成する。

    Args:
        body (UserUploadPostRequest): アップロードファイル POSTリクエストスキーマ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UserUploadResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: UserUploadPostRequest,
) -> Optional[Union[ErrorResponse, UserUploadResponse]]:
    """アップロードファイルの作成

     新しいアップロードファイルを作成する。

    Args:
        body (UserUploadPostRequest): アップロードファイル POSTリクエストスキーマ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UserUploadResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UserUploadPostRequest,
) -> Response[Union[ErrorResponse, UserUploadResponse]]:
    """アップロードファイルの作成

     新しいアップロードファイルを作成する。

    Args:
        body (UserUploadPostRequest): アップロードファイル POSTリクエストスキーマ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UserUploadResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UserUploadPostRequest,
) -> Optional[Union[ErrorResponse, UserUploadResponse]]:
    """アップロードファイルの作成

     新しいアップロードファイルを作成する。

    Args:
        body (UserUploadPostRequest): アップロードファイル POSTリクエストスキーマ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UserUploadResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
