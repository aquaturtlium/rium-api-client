from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.sensor_source_patch_request import SensorSourcePatchRequest
from ...models.sensor_source_response import SensorSourceResponse
from ...types import Response


def _get_kwargs(
    sensor_source_id: int,
    *,
    body: SensorSourcePatchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/sensor-sources/{sensor_source_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SensorSourceResponse]]:
    if response.status_code == 200:
        response_200 = SensorSourceResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SensorSourceResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sensor_source_id: int,
    *,
    client: AuthenticatedClient,
    body: SensorSourcePatchRequest,
) -> Response[Union[ErrorResponse, SensorSourceResponse]]:
    """センサソースの更新

     指定したセンサソースを更新する。

    Args:
        sensor_source_id (int):
        body (SensorSourcePatchRequest): センサソース PATCHリクエストスキーマ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SensorSourceResponse]]
    """

    kwargs = _get_kwargs(
        sensor_source_id=sensor_source_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sensor_source_id: int,
    *,
    client: AuthenticatedClient,
    body: SensorSourcePatchRequest,
) -> Optional[Union[ErrorResponse, SensorSourceResponse]]:
    """センサソースの更新

     指定したセンサソースを更新する。

    Args:
        sensor_source_id (int):
        body (SensorSourcePatchRequest): センサソース PATCHリクエストスキーマ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SensorSourceResponse]
    """

    return sync_detailed(
        sensor_source_id=sensor_source_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    sensor_source_id: int,
    *,
    client: AuthenticatedClient,
    body: SensorSourcePatchRequest,
) -> Response[Union[ErrorResponse, SensorSourceResponse]]:
    """センサソースの更新

     指定したセンサソースを更新する。

    Args:
        sensor_source_id (int):
        body (SensorSourcePatchRequest): センサソース PATCHリクエストスキーマ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SensorSourceResponse]]
    """

    kwargs = _get_kwargs(
        sensor_source_id=sensor_source_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sensor_source_id: int,
    *,
    client: AuthenticatedClient,
    body: SensorSourcePatchRequest,
) -> Optional[Union[ErrorResponse, SensorSourceResponse]]:
    """センサソースの更新

     指定したセンサソースを更新する。

    Args:
        sensor_source_id (int):
        body (SensorSourcePatchRequest): センサソース PATCHリクエストスキーマ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SensorSourceResponse]
    """

    return (
        await asyncio_detailed(
            sensor_source_id=sensor_source_id,
            client=client,
            body=body,
        )
    ).parsed
