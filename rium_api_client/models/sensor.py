from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.sensor_sensor_type_id import SensorSensorTypeId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sensor_source import SensorSource


T = TypeVar("T", bound="Sensor")


@_attrs_define
class Sensor:
    """**センサ** 計測データを記録するためのデバイス情報

    Attributes:
        id (Union[Unset, int]): センサID
        name (Union[Unset, str]): センサ名称
        sensor_hub_id (Union[Unset, int]): センサハブID
        sensor_type_id (Union[Unset, SensorSensorTypeId]): センサタイプID

            - 1: システム予約タイプ
            - 2: 手動計測センサ
            - 3: 自動計測センサ
            - 4: Home Assistant 連携デバイス
            - 100: SwitchBot 温湿度計
            - 101: SwitchBot 温湿度計プラス
            - 101: SwitchBot 防水温湿度計
            - 102: SwitchBot ハブ2
            - 103: SwitchBot プラグミニ（JP）
            - 104: SwitchBot プラグミニ（US）
        active (Union[Unset, bool]): アクティブフラグ

            `true` のときに、関連付けられたセンサソースに対して計測データの登録が可能となる。
        device_id (Union[None, Unset, str]): デバイスID

            センサハードウェアに固有のID（MACアドレスなど）を指定する。 `null` 以外の値を指定したとき、センサタイプとデバイスIDの組み合わせは一意となる必要がある。
        sensor_sources (Union[Unset, list['SensorSource']]): センサソース配列
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    sensor_hub_id: Union[Unset, int] = UNSET
    sensor_type_id: Union[Unset, SensorSensorTypeId] = UNSET
    active: Union[Unset, bool] = UNSET
    device_id: Union[None, Unset, str] = UNSET
    sensor_sources: Union[Unset, list["SensorSource"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        sensor_hub_id = self.sensor_hub_id

        sensor_type_id: Union[Unset, int] = UNSET
        if not isinstance(self.sensor_type_id, Unset):
            sensor_type_id = self.sensor_type_id.value

        active = self.active

        device_id: Union[None, Unset, str]
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
            device_id = self.device_id

        sensor_sources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sensor_sources, Unset):
            sensor_sources = []
            for sensor_sources_item_data in self.sensor_sources:
                sensor_sources_item = sensor_sources_item_data.to_dict()
                sensor_sources.append(sensor_sources_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if sensor_hub_id is not UNSET:
            field_dict["sensor_hub_id"] = sensor_hub_id
        if sensor_type_id is not UNSET:
            field_dict["sensor_type_id"] = sensor_type_id
        if active is not UNSET:
            field_dict["active"] = active
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if sensor_sources is not UNSET:
            field_dict["sensor_sources"] = sensor_sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sensor_source import SensorSource

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        sensor_hub_id = d.pop("sensor_hub_id", UNSET)

        _sensor_type_id = d.pop("sensor_type_id", UNSET)
        sensor_type_id: Union[Unset, SensorSensorTypeId]
        if isinstance(_sensor_type_id, Unset):
            sensor_type_id = UNSET
        else:
            sensor_type_id = SensorSensorTypeId(_sensor_type_id)

        active = d.pop("active", UNSET)

        def _parse_device_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_id = _parse_device_id(d.pop("device_id", UNSET))

        sensor_sources = []
        _sensor_sources = d.pop("sensor_sources", UNSET)
        for sensor_sources_item_data in _sensor_sources or []:
            sensor_sources_item = SensorSource.from_dict(sensor_sources_item_data)

            sensor_sources.append(sensor_sources_item)

        sensor = cls(
            id=id,
            name=name,
            sensor_hub_id=sensor_hub_id,
            sensor_type_id=sensor_type_id,
            active=active,
            device_id=device_id,
            sensor_sources=sensor_sources,
        )

        return sensor
