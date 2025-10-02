from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.graph_type_id import GraphTypeId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.related_ids import RelatedIds


T = TypeVar("T", bound="SensorSourcePatchRequest")


@_attrs_define
class SensorSourcePatchRequest:
    """センサソース PATCHリクエストスキーマ

    Attributes:
        name (Union[Unset, str]): センサソース名称
        sensor_id (Union[Unset, int]): センサID
        graph_type_id (Union[Unset, GraphTypeId]): グラフ種別ID

            - 1: 折れ線グラフ
            - 2: 棒グラフ
            - 3: 階段グラフ
        entity_id (Union[None, Unset, str]): エンティティID

            外部サービスとの連携時等にセンサソースを一意に特定するためのIDが必要となる場合に使用する。
        loggables (Union[Unset, RelatedIds]):
    """

    name: Union[Unset, str] = UNSET
    sensor_id: Union[Unset, int] = UNSET
    graph_type_id: Union[Unset, GraphTypeId] = UNSET
    entity_id: Union[None, Unset, str] = UNSET
    loggables: Union[Unset, "RelatedIds"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        sensor_id = self.sensor_id

        graph_type_id: Union[Unset, int] = UNSET
        if not isinstance(self.graph_type_id, Unset):
            graph_type_id = self.graph_type_id.value

        entity_id: Union[None, Unset, str]
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = self.entity_id

        loggables: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.loggables, Unset):
            loggables = self.loggables.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if sensor_id is not UNSET:
            field_dict["sensor_id"] = sensor_id
        if graph_type_id is not UNSET:
            field_dict["graph_type_id"] = graph_type_id
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if loggables is not UNSET:
            field_dict["loggables"] = loggables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.related_ids import RelatedIds

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        sensor_id = d.pop("sensor_id", UNSET)

        _graph_type_id = d.pop("graph_type_id", UNSET)
        graph_type_id: Union[Unset, GraphTypeId]
        if isinstance(_graph_type_id, Unset):
            graph_type_id = UNSET
        else:
            graph_type_id = GraphTypeId(_graph_type_id)

        def _parse_entity_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

        _loggables = d.pop("loggables", UNSET)
        loggables: Union[Unset, RelatedIds]
        if isinstance(_loggables, Unset):
            loggables = UNSET
        else:
            loggables = RelatedIds.from_dict(_loggables)

        sensor_source_patch_request = cls(
            name=name,
            sensor_id=sensor_id,
            graph_type_id=graph_type_id,
            entity_id=entity_id,
            loggables=loggables,
        )

        return sensor_source_patch_request
