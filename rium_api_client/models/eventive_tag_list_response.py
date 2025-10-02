from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.eventive_tag import EventiveTag
    from ..models.pagination import Pagination


T = TypeVar("T", bound="EventiveTagListResponse")


@_attrs_define
class EventiveTagListResponse:
    """飼育記録タグリストレスポンススキーマ

    Attributes:
        success (bool): 実行結果
        data (list['EventiveTag']): 飼育記録タグリスト
        pagination (Pagination): ページネーション情報
    """

    success: bool
    data: list["EventiveTag"]
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
        from ..models.eventive_tag import EventiveTag
        from ..models.pagination import Pagination

        d = dict(src_dict)
        success = d.pop("success")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = EventiveTag.from_dict(data_item_data)

            data.append(data_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        eventive_tag_list_response = cls(
            success=success,
            data=data,
            pagination=pagination,
        )

        return eventive_tag_list_response
