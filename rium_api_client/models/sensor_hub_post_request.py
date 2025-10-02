from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.sensor_hub_post_request_sensor_hub_type_id import SensorHubPostRequestSensorHubTypeId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.related_ids import RelatedIds
    from ..models.sensor_post_request import SensorPostRequest


T = TypeVar("T", bound="SensorHubPostRequest")


@_attrs_define
class SensorHubPostRequest:
    """センサハブ POSTリクエストスキーマ

    Attributes:
        name (str): センサハブ名称
        user_id (UUID): ユーザID
        sensor_hub_type_id (SensorHubPostRequestSensorHubTypeId): センサハブタイプID

            - 1: 手動計測用センサハブ
            - 2: 自動計測用センサハブ
            - 3: MonitoRIUM
            - 100: SwitchBot ハブ
            - 101: SwitchBot ハブミニ
            - 102: SwitchBot ハブプラス
            - 103: SwitchBot ハブ2
            - 104: SwitchBot プラグミニ（JP）
            - 105: SwitchBot プラグミニ（US）

            RIUM APIからは `2` `3` のみ指定可能であるが、 `3` は将来実装される機能向けに予約されたIDのため `2` を使用すること。
        is_auto (Union[Unset, bool]): 自動計測フラグ

            自動計測を行うセンサをまとめるハブの場合は `true`、手動計測を行うセンサをまとめるハブの場合は `false` となる。

            ユーザ登録時に `is_auto` が `false` のセンサハブ（マニュアルセンサハブ）が自動生成される。マニュアルセンサハブは1ユーザにつき1つのみ作成できるため、API経由で作成するセンサハブは全て`is_auto`
            が `true` のセンサハブ（自動計測センサハブ）となる。
        device_id (Union[None, Unset, str]): デバイスID

            センサハブハードウェアに固有のID（MACアドレスなど）を指定する。 `null` 以外の値を指定したとき、センサハブタイプとデバイスIDの組み合わせは一意となる必要がある。
        sensors (Union['RelatedIds', Unset, list['SensorPostRequest']]): 関連センサ指定情報
    """

    name: str
    user_id: UUID
    sensor_hub_type_id: SensorHubPostRequestSensorHubTypeId
    is_auto: Union[Unset, bool] = UNSET
    device_id: Union[None, Unset, str] = UNSET
    sensors: Union["RelatedIds", Unset, list["SensorPostRequest"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.related_ids import RelatedIds

        name = self.name

        user_id = str(self.user_id)

        sensor_hub_type_id = self.sensor_hub_type_id.value

        is_auto = self.is_auto

        device_id: Union[None, Unset, str]
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
            device_id = self.device_id

        sensors: Union[Unset, dict[str, Any], list[dict[str, Any]]]
        if isinstance(self.sensors, Unset):
            sensors = UNSET
        elif isinstance(self.sensors, RelatedIds):
            sensors = self.sensors.to_dict()
        else:
            sensors = []
            for componentsschemas_sensor_relation_type_1_item_data in self.sensors:
                componentsschemas_sensor_relation_type_1_item = (
                    componentsschemas_sensor_relation_type_1_item_data.to_dict()
                )
                sensors.append(componentsschemas_sensor_relation_type_1_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "user_id": user_id,
                "sensor_hub_type_id": sensor_hub_type_id,
            }
        )
        if is_auto is not UNSET:
            field_dict["is_auto"] = is_auto
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if sensors is not UNSET:
            field_dict["sensors"] = sensors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.related_ids import RelatedIds
        from ..models.sensor_post_request import SensorPostRequest

        d = dict(src_dict)
        name = d.pop("name")

        user_id = UUID(d.pop("user_id"))

        sensor_hub_type_id = SensorHubPostRequestSensorHubTypeId(d.pop("sensor_hub_type_id"))

        is_auto = d.pop("is_auto", UNSET)

        def _parse_device_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_id = _parse_device_id(d.pop("device_id", UNSET))

        def _parse_sensors(data: object) -> Union["RelatedIds", Unset, list["SensorPostRequest"]]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sensor_relation_type_0 = RelatedIds.from_dict(data)

                return componentsschemas_sensor_relation_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            componentsschemas_sensor_relation_type_1 = []
            _componentsschemas_sensor_relation_type_1 = data
            for componentsschemas_sensor_relation_type_1_item_data in _componentsschemas_sensor_relation_type_1:
                componentsschemas_sensor_relation_type_1_item = SensorPostRequest.from_dict(
                    componentsschemas_sensor_relation_type_1_item_data
                )

                componentsschemas_sensor_relation_type_1.append(componentsschemas_sensor_relation_type_1_item)

            return componentsschemas_sensor_relation_type_1

        sensors = _parse_sensors(d.pop("sensors", UNSET))

        sensor_hub_post_request = cls(
            name=name,
            user_id=user_id,
            sensor_hub_type_id=sensor_hub_type_id,
            is_auto=is_auto,
            device_id=device_id,
            sensors=sensors,
        )

        return sensor_hub_post_request
