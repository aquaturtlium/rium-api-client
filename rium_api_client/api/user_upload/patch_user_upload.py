from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.user_upload_patch_request import UserUploadPatchRequest
from ...models.user_upload_response import UserUploadResponse
from ...types import Response


def _get_kwargs(
    user_upload_id: int,
    *,
    body: UserUploadPatchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/user-uploads/{user_upload_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UserUploadResponse]]:
    if response.status_code == 200:
        response_200 = UserUploadResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UserUploadResponse]]:
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
    body: UserUploadPatchRequest,
) -> Response[Union[ErrorResponse, UserUploadResponse]]:
    """アップロードファイルの更新

     指定したアップロードファイルを更新する。

    Args:
        user_upload_id (int):
        body (UserUploadPatchRequest): アップロードファイル PATCHリクエストスキーマ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UserUploadResponse]]
    """

    kwargs = _get_kwargs(
        user_upload_id=user_upload_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_upload_id: int,
    *,
    client: AuthenticatedClient,
    body: UserUploadPatchRequest,
) -> Optional[Union[ErrorResponse, UserUploadResponse]]:
    """アップロードファイルの更新

     指定したアップロードファイルを更新する。

    Args:
        user_upload_id (int):
        body (UserUploadPatchRequest): アップロードファイル PATCHリクエストスキーマ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UserUploadResponse]
    """

    return sync_detailed(
        user_upload_id=user_upload_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_upload_id: int,
    *,
    client: AuthenticatedClient,
    body: UserUploadPatchRequest,
) -> Response[Union[ErrorResponse, UserUploadResponse]]:
    """アップロードファイルの更新

     指定したアップロードファイルを更新する。

    Args:
        user_upload_id (int):
        body (UserUploadPatchRequest): アップロードファイル PATCHリクエストスキーマ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UserUploadResponse]]
    """

    kwargs = _get_kwargs(
        user_upload_id=user_upload_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_upload_id: int,
    *,
    client: AuthenticatedClient,
    body: UserUploadPatchRequest,
) -> Optional[Union[ErrorResponse, UserUploadResponse]]:
    """アップロードファイルの更新

     指定したアップロードファイルを更新する。

    Args:
        user_upload_id (int):
        body (UserUploadPatchRequest): アップロードファイル PATCHリクエストスキーマ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UserUploadResponse]
    """

    return (
        await asyncio_detailed(
            user_upload_id=user_upload_id,
            client=client,
            body=body,
        )
    ).parsed
