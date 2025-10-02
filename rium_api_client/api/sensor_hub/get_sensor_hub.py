from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.sensor_hub_response import SensorHubResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sensor_hub_id: int,
    *,
    includes: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["includes"] = includes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/sensor-hubs/{sensor_hub_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SensorHubResponse]]:
    if response.status_code == 200:
        response_200 = SensorHubResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SensorHubResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sensor_hub_id: int,
    *,
    client: AuthenticatedClient,
    includes: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, SensorHubResponse]]:
    """センサハブの詳細表示

     指定したセンサハブの詳細を取得する。

    Args:
        sensor_hub_id (int):
        includes (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SensorHubResponse]]
    """

    kwargs = _get_kwargs(
        sensor_hub_id=sensor_hub_id,
        includes=includes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sensor_hub_id: int,
    *,
    client: AuthenticatedClient,
    includes: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, SensorHubResponse]]:
    """センサハブの詳細表示

     指定したセンサハブの詳細を取得する。

    Args:
        sensor_hub_id (int):
        includes (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SensorHubResponse]
    """

    return sync_detailed(
        sensor_hub_id=sensor_hub_id,
        client=client,
        includes=includes,
    ).parsed


async def asyncio_detailed(
    sensor_hub_id: int,
    *,
    client: AuthenticatedClient,
    includes: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, SensorHubResponse]]:
    """センサハブの詳細表示

     指定したセンサハブの詳細を取得する。

    Args:
        sensor_hub_id (int):
        includes (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SensorHubResponse]]
    """

    kwargs = _get_kwargs(
        sensor_hub_id=sensor_hub_id,
        includes=includes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sensor_hub_id: int,
    *,
    client: AuthenticatedClient,
    includes: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, SensorHubResponse]]:
    """センサハブの詳細表示

     指定したセンサハブの詳細を取得する。

    Args:
        sensor_hub_id (int):
        includes (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SensorHubResponse]
    """

    return (
        await asyncio_detailed(
            sensor_hub_id=sensor_hub_id,
            client=client,
            includes=includes,
        )
    ).parsed
