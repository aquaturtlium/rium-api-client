from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.log import Log


T = TypeVar("T", bound="LogResponse")


@_attrs_define
class LogResponse:
    """計測データレスポンススキーマ

    Attributes:
        success (bool): 実行結果
        data (Log): **計測データ** 飼育生体・飼育環境に対する数値データ
    """

    success: bool
    data: "Log"

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        data = self.data.to_dict()

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

        data = Log.from_dict(d.pop("data"))

        log_response = cls(
            success=success,
            data=data,
        )

        return log_response
