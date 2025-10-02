from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.sensor_hub_sensor_hub_type_id import SensorHubSensorHubTypeId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sensor import Sensor


T = TypeVar("T", bound="SensorHub")


@_attrs_define
class SensorHub:
    """**センサハブ** ネットワーク接続時等に複数のセンサ情報をまとめるハブデバイス情報

    Attributes:
        id (Union[Unset, int]): センサハブID
        name (Union[Unset, str]): センサハブ名称
        user_id (Union[Unset, UUID]): ユーザID
        is_auto (Union[Unset, bool]): 自動計測フラグ

            自動計測を行うセンサをまとめるハブの場合は `true`、手動計測を行うセンサをまとめるハブの場合は `false` となる。

            ユーザ登録時に `is_auto` が `false` のセンサハブ（マニュアルセンサハブ）が自動生成される。マニュアルセンサハブは1ユーザにつき1つのみ作成できるため、API経由で作成するセンサハブは全て`is_auto`
            が `true` のセンサハブ（自動計測センサハブ）となる。
        device_id (Union[None, Unset, str]): デバイスID

            センサハブハードウェアに固有のID（MACアドレスなど）を指定する。 `null` 以外の値を指定したとき、センサハブタイプとデバイスIDの組み合わせは一意となる必要がある。
        sensor_hub_type_id (Union[Unset, SensorHubSensorHubTypeId]): センサハブタイプID

            - 1: 手動計測用センサハブ
            - 2: 自動計測用センサハブ
            - 3: MonitoRIUM
            - 100: SwitchBot ハブ
            - 101: SwitchBot ハブミニ
            - 102: SwitchBot ハブプラス
            - 103: SwitchBot ハブ2
            - 104: SwitchBot プラグミニ（JP）
            - 105: SwitchBot プラグミニ（US）
        sensors (Union[Unset, list['Sensor']]): センサ配列
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    user_id: Union[Unset, UUID] = UNSET
    is_auto: Union[Unset, bool] = UNSET
    device_id: Union[None, Unset, str] = UNSET
    sensor_hub_type_id: Union[Unset, SensorHubSensorHubTypeId] = UNSET
    sensors: Union[Unset, list["Sensor"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        user_id: Union[Unset, str] = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        is_auto = self.is_auto

        device_id: Union[None, Unset, str]
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
            device_id = self.device_id

        sensor_hub_type_id: Union[Unset, int] = UNSET
        if not isinstance(self.sensor_hub_type_id, Unset):
            sensor_hub_type_id = self.sensor_hub_type_id.value

        sensors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sensors, Unset):
            sensors = []
            for sensors_item_data in self.sensors:
                sensors_item = sensors_item_data.to_dict()
                sensors.append(sensors_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if is_auto is not UNSET:
            field_dict["is_auto"] = is_auto
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if sensor_hub_type_id is not UNSET:
            field_dict["sensor_hub_type_id"] = sensor_hub_type_id
        if sensors is not UNSET:
            field_dict["sensors"] = sensors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sensor import Sensor

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _user_id = d.pop("user_id", UNSET)
        user_id: Union[Unset, UUID]
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        is_auto = d.pop("is_auto", UNSET)

        def _parse_device_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_id = _parse_device_id(d.pop("device_id", UNSET))

        _sensor_hub_type_id = d.pop("sensor_hub_type_id", UNSET)
        sensor_hub_type_id: Union[Unset, SensorHubSensorHubTypeId]
        if isinstance(_sensor_hub_type_id, Unset):
            sensor_hub_type_id = UNSET
        else:
            sensor_hub_type_id = SensorHubSensorHubTypeId(_sensor_hub_type_id)

        sensors = []
        _sensors = d.pop("sensors", UNSET)
        for sensors_item_data in _sensors or []:
            sensors_item = Sensor.from_dict(sensors_item_data)

            sensors.append(sensors_item)

        sensor_hub = cls(
            id=id,
            name=name,
            user_id=user_id,
            is_auto=is_auto,
            device_id=device_id,
            sensor_hub_type_id=sensor_hub_type_id,
            sensors=sensors,
        )

        return sensor_hub
