from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUploadPatchRequest")


@_attrs_define
class UserUploadPatchRequest:
    """アップロードファイル PATCHリクエストスキーマ

    Attributes:
        attachable_id (Union[None, Unset, int]): 添付対象ID
        display_priority (Union[Unset, int]): 表示優先度

            優先度が高いものから順に表示される。
    """

    attachable_id: Union[None, Unset, int] = UNSET
    display_priority: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        attachable_id: Union[None, Unset, int]
        if isinstance(self.attachable_id, Unset):
            attachable_id = UNSET
        else:
            attachable_id = self.attachable_id

        display_priority = self.display_priority

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if attachable_id is not UNSET:
            field_dict["attachable_id"] = attachable_id
        if display_priority is not UNSET:
            field_dict["display_priority"] = display_priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_attachable_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        attachable_id = _parse_attachable_id(d.pop("attachable_id", UNSET))

        display_priority = d.pop("display_priority", UNSET)

        user_upload_patch_request = cls(
            attachable_id=attachable_id,
            display_priority=display_priority,
        )

        return user_upload_patch_request
