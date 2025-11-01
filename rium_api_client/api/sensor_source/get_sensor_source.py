from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.sensor_source_response import SensorSourceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sensor_source_id: int,
    *,
    fields: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/sensor-sources/{sensor_source_id}",
        "params": params,
    }

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
    fields: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, SensorSourceResponse]]:
    """センサソースの詳細表示

     指定したセンサソースの詳細を取得する。

    Args:
        sensor_source_id (int):
        fields (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SensorSourceResponse]]
    """

    kwargs = _get_kwargs(
        sensor_source_id=sensor_source_id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sensor_source_id: int,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, SensorSourceResponse]]:
    """センサソースの詳細表示

     指定したセンサソースの詳細を取得する。

    Args:
        sensor_source_id (int):
        fields (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SensorSourceResponse]
    """

    return sync_detailed(
        sensor_source_id=sensor_source_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    sensor_source_id: int,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, SensorSourceResponse]]:
    """センサソースの詳細表示

     指定したセンサソースの詳細を取得する。

    Args:
        sensor_source_id (int):
        fields (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SensorSourceResponse]]
    """

    kwargs = _get_kwargs(
        sensor_source_id=sensor_source_id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sensor_source_id: int,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, SensorSourceResponse]]:
    """センサソースの詳細表示

     指定したセンサソースの詳細を取得する。

    Args:
        sensor_source_id (int):
        fields (Union[Unset, str]):

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
            fields=fields,
        )
    ).parsed
