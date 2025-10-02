from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventiveTag")


@_attrs_define
class EventiveTag:
    """**飼育記録タグ** 飼育記録に付与するタグ情報

    Attributes:
        id (Union[Unset, int]): 飼育記録タグID
        name (Union[Unset, str]): 飼育記録タグ名称
        is_default (Union[Unset, bool]): 一般的なタグフラグ

            `true` の場合、**一般的なタグ**として飼育記録をつける際の選択肢として表示されます。
             Default: False.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = False

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_default = self.is_default

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_default is not UNSET:
            field_dict["is_default"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        is_default = d.pop("is_default", UNSET)

        eventive_tag = cls(
            id=id,
            name=name,
            is_default=is_default,
        )

        return eventive_tag
