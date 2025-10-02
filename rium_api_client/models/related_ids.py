from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="RelatedIds")


@_attrs_define
class RelatedIds:
    """
    Attributes:
        field_ids (list[int]): 関連ID配列
    """

    field_ids: list[int]

    def to_dict(self) -> dict[str, Any]:
        field_ids = self.field_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "_ids": field_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_ids = cast(list[int], d.pop("_ids"))

        related_ids = cls(
            field_ids=field_ids,
        )

        return related_ids
