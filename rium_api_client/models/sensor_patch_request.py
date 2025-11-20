from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.related_ids import RelatedIds
    from ..models.sensor_source_post_request import SensorSourcePostRequest


T = TypeVar("T", bound="SensorPatchRequest")


@_attrs_define
class SensorPatchRequest:
    """センサ PATCHリクエストスキーマ

    Attributes:
        name (Union[Unset, str]): センサ名称
        sensor_hub_id (Union[Unset, int]): センサハブID
        is_active (Union[Unset, bool]): アクティブフラグ

            `true` のときに、関連付けられたセンサソースに対して計測データの登録が可能となる。
        device_id (Union[None, Unset, str]): デバイスID

            センサハードウェアに固有のID（MACアドレスなど）を指定する。 `null` 以外の値を指定したとき、センサタイプとデバイスIDの組み合わせは一意となる必要がある。
        sensor_sources (Union['RelatedIds', Unset, list['SensorSourcePostRequest']]): 関連センサソース指定情報
    """

    name: Union[Unset, str] = UNSET
    sensor_hub_id: Union[Unset, int] = UNSET
    is_active: Union[Unset, bool] = UNSET
    device_id: Union[None, Unset, str] = UNSET
    sensor_sources: Union["RelatedIds", Unset, list["SensorSourcePostRequest"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.related_ids import RelatedIds

        name = self.name

        sensor_hub_id = self.sensor_hub_id

        is_active = self.is_active

        device_id: Union[None, Unset, str]
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
            device_id = self.device_id

        sensor_sources: Union[Unset, dict[str, Any], list[dict[str, Any]]]
        if isinstance(self.sensor_sources, Unset):
            sensor_sources = UNSET
        elif isinstance(self.sensor_sources, RelatedIds):
            sensor_sources = self.sensor_sources.to_dict()
        else:
            sensor_sources = []
            for componentsschemas_sensor_source_relation_type_1_item_data in self.sensor_sources:
                componentsschemas_sensor_source_relation_type_1_item = (
                    componentsschemas_sensor_source_relation_type_1_item_data.to_dict()
                )
                sensor_sources.append(componentsschemas_sensor_source_relation_type_1_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if sensor_hub_id is not UNSET:
            field_dict["sensor_hub_id"] = sensor_hub_id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if sensor_sources is not UNSET:
            field_dict["sensor_sources"] = sensor_sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.related_ids import RelatedIds
        from ..models.sensor_source_post_request import SensorSourcePostRequest

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        sensor_hub_id = d.pop("sensor_hub_id", UNSET)

        is_active = d.pop("is_active", UNSET)

        def _parse_device_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_id = _parse_device_id(d.pop("device_id", UNSET))

        def _parse_sensor_sources(data: object) -> Union["RelatedIds", Unset, list["SensorSourcePostRequest"]]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sensor_source_relation_type_0 = RelatedIds.from_dict(data)

                return componentsschemas_sensor_source_relation_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            componentsschemas_sensor_source_relation_type_1 = []
            _componentsschemas_sensor_source_relation_type_1 = data
            for (
                componentsschemas_sensor_source_relation_type_1_item_data
            ) in _componentsschemas_sensor_source_relation_type_1:
                componentsschemas_sensor_source_relation_type_1_item = SensorSourcePostRequest.from_dict(
                    componentsschemas_sensor_source_relation_type_1_item_data
                )

                componentsschemas_sensor_source_relation_type_1.append(
                    componentsschemas_sensor_source_relation_type_1_item
                )

            return componentsschemas_sensor_source_relation_type_1

        sensor_sources = _parse_sensor_sources(d.pop("sensor_sources", UNSET))

        sensor_patch_request = cls(
            name=name,
            sensor_hub_id=sensor_hub_id,
            is_active=is_active,
            device_id=device_id,
            sensor_sources=sensor_sources,
        )

        return sensor_patch_request
