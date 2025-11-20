from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.graph_type_id import GraphTypeId
from ..models.sensor_source_type_id import SensorSourceTypeId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.loggable import Loggable


T = TypeVar("T", bound="SensorSource")


@_attrs_define
class SensorSource:
    """**センサソース** センサが取得できる信号の情報

    Attributes:
        id (Union[Unset, int]): センサソースID
        name (Union[Unset, str]): センサソース名称

            `名称[単位]` 形式で指定することで、センサソース名称と計測単位を指定できる。例えば `水温[℃]` のように指定する。
        sensor_id (Union[Unset, int]): センサID
        sensor_source_type_id (Union[Unset, SensorSourceTypeId]): センサソースタイプID

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
        name_wo_unit (Union[Unset, str]): センサソース名称（単位なし）

            センサソース名称から計測単位を除いた文字列
        unit (Union[Unset, str]): センサソース計測単位
        loggables (Union[Unset, list['Loggable']]): 記録対象配列
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    sensor_id: Union[Unset, int] = UNSET
    sensor_source_type_id: Union[Unset, SensorSourceTypeId] = UNSET
    graph_type_id: Union[Unset, GraphTypeId] = UNSET
    entity_id: Union[None, Unset, str] = UNSET
    name_wo_unit: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    loggables: Union[Unset, list["Loggable"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        sensor_id = self.sensor_id

        sensor_source_type_id: Union[Unset, int] = UNSET
        if not isinstance(self.sensor_source_type_id, Unset):
            sensor_source_type_id = self.sensor_source_type_id.value

        graph_type_id: Union[Unset, int] = UNSET
        if not isinstance(self.graph_type_id, Unset):
            graph_type_id = self.graph_type_id.value

        entity_id: Union[None, Unset, str]
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = self.entity_id

        name_wo_unit = self.name_wo_unit

        unit = self.unit

        loggables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.loggables, Unset):
            loggables = []
            for loggables_item_data in self.loggables:
                loggables_item = loggables_item_data.to_dict()
                loggables.append(loggables_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if sensor_id is not UNSET:
            field_dict["sensor_id"] = sensor_id
        if sensor_source_type_id is not UNSET:
            field_dict["sensor_source_type_id"] = sensor_source_type_id
        if graph_type_id is not UNSET:
            field_dict["graph_type_id"] = graph_type_id
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if name_wo_unit is not UNSET:
            field_dict["name_wo_unit"] = name_wo_unit
        if unit is not UNSET:
            field_dict["unit"] = unit
        if loggables is not UNSET:
            field_dict["loggables"] = loggables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.loggable import Loggable

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        sensor_id = d.pop("sensor_id", UNSET)

        _sensor_source_type_id = d.pop("sensor_source_type_id", UNSET)
        sensor_source_type_id: Union[Unset, SensorSourceTypeId]
        if isinstance(_sensor_source_type_id, Unset):
            sensor_source_type_id = UNSET
        else:
            sensor_source_type_id = SensorSourceTypeId(_sensor_source_type_id)

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

        name_wo_unit = d.pop("name_wo_unit", UNSET)

        unit = d.pop("unit", UNSET)

        loggables = []
        _loggables = d.pop("loggables", UNSET)
        for loggables_item_data in _loggables or []:
            loggables_item = Loggable.from_dict(loggables_item_data)

            loggables.append(loggables_item)

        sensor_source = cls(
            id=id,
            name=name,
            sensor_id=sensor_id,
            sensor_source_type_id=sensor_source_type_id,
            graph_type_id=graph_type_id,
            entity_id=entity_id,
            name_wo_unit=name_wo_unit,
            unit=unit,
            loggables=loggables,
        )

        return sensor_source
