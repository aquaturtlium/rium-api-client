from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_sensor_hubs_of_user_direction import GetSensorHubsOfUserDirection
from ...models.get_sensor_hubs_of_user_sort import GetSensorHubsOfUserSort
from ...models.sensor_hub_list_response import SensorHubListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: UUID,
    *,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetSensorHubsOfUserSort] = GetSensorHubsOfUserSort.IS_AUTO,
    direction: Union[Unset, GetSensorHubsOfUserDirection] = GetSensorHubsOfUserDirection.DESC,
    device_id: Union[Unset, str] = UNSET,
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

    params["device_id"] = device_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/users/{user_id}/sensor-hubs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SensorHubListResponse]]:
    if response.status_code == 200:
        response_200 = SensorHubListResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SensorHubListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetSensorHubsOfUserSort] = GetSensorHubsOfUserSort.IS_AUTO,
    direction: Union[Unset, GetSensorHubsOfUserDirection] = GetSensorHubsOfUserDirection.DESC,
    device_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, SensorHubListResponse]]:
    """センサハブの一覧表示

     指定したユーザに紐づくセンサハブの一覧を取得する。

    Args:
        user_id (UUID):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetSensorHubsOfUserSort]):  Default: GetSensorHubsOfUserSort.IS_AUTO.
        direction (Union[Unset, GetSensorHubsOfUserDirection]):  Default:
            GetSensorHubsOfUserDirection.DESC.
        device_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SensorHubListResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        fields=fields,
        limit=limit,
        page=page,
        sort=sort,
        direction=direction,
        device_id=device_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetSensorHubsOfUserSort] = GetSensorHubsOfUserSort.IS_AUTO,
    direction: Union[Unset, GetSensorHubsOfUserDirection] = GetSensorHubsOfUserDirection.DESC,
    device_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, SensorHubListResponse]]:
    """センサハブの一覧表示

     指定したユーザに紐づくセンサハブの一覧を取得する。

    Args:
        user_id (UUID):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetSensorHubsOfUserSort]):  Default: GetSensorHubsOfUserSort.IS_AUTO.
        direction (Union[Unset, GetSensorHubsOfUserDirection]):  Default:
            GetSensorHubsOfUserDirection.DESC.
        device_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SensorHubListResponse]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        fields=fields,
        limit=limit,
        page=page,
        sort=sort,
        direction=direction,
        device_id=device_id,
    ).parsed


async def asyncio_detailed(
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetSensorHubsOfUserSort] = GetSensorHubsOfUserSort.IS_AUTO,
    direction: Union[Unset, GetSensorHubsOfUserDirection] = GetSensorHubsOfUserDirection.DESC,
    device_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, SensorHubListResponse]]:
    """センサハブの一覧表示

     指定したユーザに紐づくセンサハブの一覧を取得する。

    Args:
        user_id (UUID):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetSensorHubsOfUserSort]):  Default: GetSensorHubsOfUserSort.IS_AUTO.
        direction (Union[Unset, GetSensorHubsOfUserDirection]):  Default:
            GetSensorHubsOfUserDirection.DESC.
        device_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SensorHubListResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        fields=fields,
        limit=limit,
        page=page,
        sort=sort,
        direction=direction,
        device_id=device_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, GetSensorHubsOfUserSort] = GetSensorHubsOfUserSort.IS_AUTO,
    direction: Union[Unset, GetSensorHubsOfUserDirection] = GetSensorHubsOfUserDirection.DESC,
    device_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, SensorHubListResponse]]:
    """センサハブの一覧表示

     指定したユーザに紐づくセンサハブの一覧を取得する。

    Args:
        user_id (UUID):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):  Default: 1.
        sort (Union[Unset, GetSensorHubsOfUserSort]):  Default: GetSensorHubsOfUserSort.IS_AUTO.
        direction (Union[Unset, GetSensorHubsOfUserDirection]):  Default:
            GetSensorHubsOfUserDirection.DESC.
        device_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SensorHubListResponse]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            fields=fields,
            limit=limit,
            page=page,
            sort=sort,
            direction=direction,
            device_id=device_id,
        )
    ).parsed
