import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.log_response import LogResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    time: datetime.datetime,
    sensor_source_id: int,
    loggable_id: int,
    fields: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_time = time.isoformat()
    params["time"] = json_time

    params["sensor_source_id"] = sensor_source_id

    params["loggable_id"] = loggable_id

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, LogResponse]]:
    if response.status_code == 200:
        response_200 = LogResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, LogResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    time: datetime.datetime,
    sensor_source_id: int,
    loggable_id: int,
    fields: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, LogResponse]]:
    """計測データの詳細表示

     指定した計測データの詳細を取得する。

    Args:
        time (datetime.datetime):
        sensor_source_id (int):
        loggable_id (int):
        fields (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, LogResponse]]
    """

    kwargs = _get_kwargs(
        time=time,
        sensor_source_id=sensor_source_id,
        loggable_id=loggable_id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    time: datetime.datetime,
    sensor_source_id: int,
    loggable_id: int,
    fields: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, LogResponse]]:
    """計測データの詳細表示

     指定した計測データの詳細を取得する。

    Args:
        time (datetime.datetime):
        sensor_source_id (int):
        loggable_id (int):
        fields (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, LogResponse]
    """

    return sync_detailed(
        client=client,
        time=time,
        sensor_source_id=sensor_source_id,
        loggable_id=loggable_id,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    time: datetime.datetime,
    sensor_source_id: int,
    loggable_id: int,
    fields: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, LogResponse]]:
    """計測データの詳細表示

     指定した計測データの詳細を取得する。

    Args:
        time (datetime.datetime):
        sensor_source_id (int):
        loggable_id (int):
        fields (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, LogResponse]]
    """

    kwargs = _get_kwargs(
        time=time,
        sensor_source_id=sensor_source_id,
        loggable_id=loggable_id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    time: datetime.datetime,
    sensor_source_id: int,
    loggable_id: int,
    fields: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, LogResponse]]:
    """計測データの詳細表示

     指定した計測データの詳細を取得する。

    Args:
        time (datetime.datetime):
        sensor_source_id (int):
        loggable_id (int):
        fields (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, LogResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            time=time,
            sensor_source_id=sensor_source_id,
            loggable_id=loggable_id,
            fields=fields,
        )
    ).parsed
