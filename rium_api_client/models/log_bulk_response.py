from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.log import Log


T = TypeVar("T", bound="LogBulkResponse")


@_attrs_define
class LogBulkResponse:
    """一括登録時計測データレスポンススキーマ

    Attributes:
        success (bool): 実行結果
        data (list['Log']): 計測データ配列
    """

    success: bool
    data: list["Log"]

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "success": success,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log import Log

        d = dict(src_dict)
        success = d.pop("success")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Log.from_dict(data_item_data)

            data.append(data_item)

        log_bulk_response = cls(
            success=success,
            data=data,
        )

        return log_bulk_response
