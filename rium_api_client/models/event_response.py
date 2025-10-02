from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.event import Event


T = TypeVar("T", bound="EventResponse")


@_attrs_define
class EventResponse:
    """飼育記録レスポンススキーマ

    Attributes:
        success (bool): 実行結果
        data (Event): **飼育記録** 飼育生体・飼育環境に対するテキストベースの記録
    """

    success: bool
    data: "Event"

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
        from ..models.event import Event

        d = dict(src_dict)
        success = d.pop("success")

        data = Event.from_dict(d.pop("data"))

        event_response = cls(
            success=success,
            data=data,
        )

        return event_response
