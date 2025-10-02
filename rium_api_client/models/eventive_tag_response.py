from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.eventive_tag import EventiveTag


T = TypeVar("T", bound="EventiveTagResponse")


@_attrs_define
class EventiveTagResponse:
    """
    Attributes:
        success (bool): 実行結果
        data (EventiveTag): **飼育記録タグ** 飼育記録に付与するタグ情報
    """

    success: bool
    data: "EventiveTag"

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
        from ..models.eventive_tag import EventiveTag

        d = dict(src_dict)
        success = d.pop("success")

        data = EventiveTag.from_dict(d.pop("data"))

        eventive_tag_response = cls(
            success=success,
            data=data,
        )

        return eventive_tag_response
