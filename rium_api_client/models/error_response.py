from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.error import Error


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """エラーレスポンススキーマ

    Attributes:
        success (bool): 実行結果 Default: False.
        data (Error): エラー
    """

    data: "Error"
    success: bool = False

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
        from ..models.error import Error

        d = dict(src_dict)
        success = d.pop("success")

        data = Error.from_dict(d.pop("data"))

        error_response = cls(
            success=success,
            data=data,
        )

        return error_response
