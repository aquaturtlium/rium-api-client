from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.sensor_source import SensorSource


T = TypeVar("T", bound="SensorSourceListResponse")


@_attrs_define
class SensorSourceListResponse:
    """センサソースリストレスポンススキーマ

    Attributes:
        success (bool): 実行結果
        data (list['SensorSource']): センサソースリスト
        pagination (Pagination): ページネーション情報
    """

    success: bool
    data: list["SensorSource"]
    pagination: "Pagination"

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "success": success,
                "data": data,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.sensor_source import SensorSource

        d = dict(src_dict)
        success = d.pop("success")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = SensorSource.from_dict(data_item_data)

            data.append(data_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        sensor_source_list_response = cls(
            success=success,
            data=data,
            pagination=pagination,
        )

        return sensor_source_list_response
