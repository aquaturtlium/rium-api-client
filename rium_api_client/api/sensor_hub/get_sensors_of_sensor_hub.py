from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_sensors_of_sensor_hub_direction import GetSensorsOfSensorHubDirection
from ...models.get_sensors_of_sensor_hub_sort import GetSensorsOfSensorHubSort
from ...models.sensor_list_response import SensorListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sensor_hub_id: int,
    *,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetSensorsOfSensorHubSort] = GetSensorsOfSensorHubSort.ACTIVE,
    direction: Union[Unset, GetSensorsOfSensorHubDirection] = GetSensorsOfSensorHubDirection.DESC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["fields"] = fields

    params["limit"] = limit

    params["page"] = page

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_direction: Union[Unset, str] = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/sensor-hubs/{sensor_hub_id}/sensors",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SensorListResponse]]:
    if response.status_code == 200:
        response_200 = SensorListResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SensorListResponse]]:
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
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetSensorsOfSensorHubSort] = GetSensorsOfSensorHubSort.ACTIVE,
    direction: Union[Unset, GetSensorsOfSensorHubDirection] = GetSensorsOfSensorHubDirection.DESC,
) -> Response[Union[ErrorResponse, SensorListResponse]]:
    """センサの一覧表示

     指定したセンサハブに属するセンサの一覧を取得する。

    Args:
        sensor_hub_id (int):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetSensorsOfSensorHubSort]):  Default:
            GetSensorsOfSensorHubSort.ACTIVE.
        direction (Union[Unset, GetSensorsOfSensorHubDirection]):  Default:
            GetSensorsOfSensorHubDirection.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SensorListResponse]]
    """

    kwargs = _get_kwargs(
        sensor_hub_id=sensor_hub_id,
        fields=fields,
        limit=limit,
        page=page,
        sort=sort,
        direction=direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sensor_hub_id: int,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetSensorsOfSensorHubSort] = GetSensorsOfSensorHubSort.ACTIVE,
    direction: Union[Unset, GetSensorsOfSensorHubDirection] = GetSensorsOfSensorHubDirection.DESC,
) -> Optional[Union[ErrorResponse, SensorListResponse]]:
    """センサの一覧表示

     指定したセンサハブに属するセンサの一覧を取得する。

    Args:
        sensor_hub_id (int):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetSensorsOfSensorHubSort]):  Default:
            GetSensorsOfSensorHubSort.ACTIVE.
        direction (Union[Unset, GetSensorsOfSensorHubDirection]):  Default:
            GetSensorsOfSensorHubDirection.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SensorListResponse]
    """

    return sync_detailed(
        sensor_hub_id=sensor_hub_id,
        client=client,
        fields=fields,
        limit=limit,
        page=page,
        sort=sort,
        direction=direction,
    ).parsed


async def asyncio_detailed(
    sensor_hub_id: int,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetSensorsOfSensorHubSort] = GetSensorsOfSensorHubSort.ACTIVE,
    direction: Union[Unset, GetSensorsOfSensorHubDirection] = GetSensorsOfSensorHubDirection.DESC,
) -> Response[Union[ErrorResponse, SensorListResponse]]:
    """センサの一覧表示

     指定したセンサハブに属するセンサの一覧を取得する。

    Args:
        sensor_hub_id (int):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetSensorsOfSensorHubSort]):  Default:
            GetSensorsOfSensorHubSort.ACTIVE.
        direction (Union[Unset, GetSensorsOfSensorHubDirection]):  Default:
            GetSensorsOfSensorHubDirection.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SensorListResponse]]
    """

    kwargs = _get_kwargs(
        sensor_hub_id=sensor_hub_id,
        fields=fields,
        limit=limit,
        page=page,
        sort=sort,
        direction=direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sensor_hub_id: int,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetSensorsOfSensorHubSort] = GetSensorsOfSensorHubSort.ACTIVE,
    direction: Union[Unset, GetSensorsOfSensorHubDirection] = GetSensorsOfSensorHubDirection.DESC,
) -> Optional[Union[ErrorResponse, SensorListResponse]]:
    """センサの一覧表示

     指定したセンサハブに属するセンサの一覧を取得する。

    Args:
        sensor_hub_id (int):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetSensorsOfSensorHubSort]):  Default:
            GetSensorsOfSensorHubSort.ACTIVE.
        direction (Union[Unset, GetSensorsOfSensorHubDirection]):  Default:
            GetSensorsOfSensorHubDirection.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SensorListResponse]
    """

    return (
        await asyncio_detailed(
            sensor_hub_id=sensor_hub_id,
            client=client,
            fields=fields,
            limit=limit,
            page=page,
            sort=sort,
            direction=direction,
        )
    ).parsed
