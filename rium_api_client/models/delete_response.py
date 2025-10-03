from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="DeleteResponse")


@_attrs_define
class DeleteResponse:
    """削除時レスポンススキーマ

    Attributes:
        success (bool): 実行結果
        data (list[Any]): 空配列
    """

    success: bool
    data: list[Any]

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        data = self.data

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
        d = dict(src_dict)
        success = d.pop("success")

        data = cast(list[Any], d.pop("data"))

        delete_response = cls(
            success=success,
            data=data,
        )

        return delete_response
