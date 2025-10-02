from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_sensor_hub_response_200 import DeleteSensorHubResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    sensor_hub_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/sensor-hubs/{sensor_hub_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteSensorHubResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DeleteSensorHubResponse200.from_dict(response.json())

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
) -> Response[Union[DeleteSensorHubResponse200, ErrorResponse]]:
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
) -> Response[Union[DeleteSensorHubResponse200, ErrorResponse]]:
    """センサハブの削除

     指定したセンサハブを削除する。

    Args:
        sensor_hub_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteSensorHubResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sensor_hub_id=sensor_hub_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sensor_hub_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DeleteSensorHubResponse200, ErrorResponse]]:
    """センサハブの削除

     指定したセンサハブを削除する。

    Args:
        sensor_hub_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteSensorHubResponse200, ErrorResponse]
    """

    return sync_detailed(
        sensor_hub_id=sensor_hub_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sensor_hub_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[DeleteSensorHubResponse200, ErrorResponse]]:
    """センサハブの削除

     指定したセンサハブを削除する。

    Args:
        sensor_hub_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteSensorHubResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        sensor_hub_id=sensor_hub_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sensor_hub_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DeleteSensorHubResponse200, ErrorResponse]]:
    """センサハブの削除

     指定したセンサハブを削除する。

    Args:
        sensor_hub_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteSensorHubResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            sensor_hub_id=sensor_hub_id,
            client=client,
        )
    ).parsed
