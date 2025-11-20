from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.graph_type_id import GraphTypeId
from ..models.sensor_source_type_id import SensorSourceTypeId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.related_ids import RelatedIds


T = TypeVar("T", bound="SensorSourcePostRequest")


@_attrs_define
class SensorSourcePostRequest:
    """センサソース POSTリクエストスキーマ

    Attributes:
        name (str): センサソース名称

            `名称[単位]` 形式で指定することで、センサソース名称と計測単位を指定できる。例えば `水温[℃]` のように指定する。
        sensor_id (int): センサID
        sensor_source_type_id (SensorSourceTypeId): センサソースタイプID

            - 1: 水温
            - 2: pH
            - 3: 気温
            - 4: 湿度
            - 5: EC
            - 6: TDS
            - 900: ディスクリート（ON/OFF等の離散値信号）
            - 999: その他
        graph_type_id (Union[Unset, GraphTypeId]): グラフ種別ID

            - 1: 折れ線グラフ
            - 2: 棒グラフ
            - 3: 階段グラフ
        entity_id (Union[None, Unset, str]): エンティティID

            外部サービスとの連携時等にセンサソースを一意に特定するためのIDが必要となる場合に使用する。
        loggables (Union[Unset, RelatedIds]):
    """

    name: str
    sensor_id: int
    sensor_source_type_id: SensorSourceTypeId
    graph_type_id: Union[Unset, GraphTypeId] = UNSET
    entity_id: Union[None, Unset, str] = UNSET
    loggables: Union[Unset, "RelatedIds"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        sensor_id = self.sensor_id

        sensor_source_type_id = self.sensor_source_type_id.value

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

        field_dict.update(
            {
                "name": name,
                "sensor_id": sensor_id,
                "sensor_source_type_id": sensor_source_type_id,
            }
        )
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
        name = d.pop("name")

        sensor_id = d.pop("sensor_id")

        sensor_source_type_id = SensorSourceTypeId(d.pop("sensor_source_type_id"))

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

        sensor_source_post_request = cls(
            name=name,
            sensor_id=sensor_id,
            sensor_source_type_id=sensor_source_type_id,
            graph_type_id=graph_type_id,
            entity_id=entity_id,
            loggables=loggables,
        )

        return sensor_source_post_request
