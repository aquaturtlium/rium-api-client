from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="EventiveTagPostRequest")


@_attrs_define
class EventiveTagPostRequest:
    """飼育記録タグ POSTリクエストスキーマ

    Attributes:
        name (str): 飼育記録タグ名称
    """

    name: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        eventive_tag_post_request = cls(
            name=name,
        )

        return eventive_tag_post_request
