from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="UserUploadPostRequest")


@_attrs_define
class UserUploadPostRequest:
    """アップロードファイル POSTリクエストスキーマ

    Attributes:
        name (File): アップロードファイルデータ

            以下の条件を満たすファイルのみアップロード可能
            - MIMEタイプ： `image/jpeg` `image/png` のいずれか
            - 拡張子： `jpeg` `jpg` `png` のいずれか
            - 画像サイズ： 縦・横ともに100px以上
            - ファイルサイズ： 1ファイルあたり5MB以下
            - 画素数： JPEG画像の場合2,400万画素、PNG画像の場合1,200万画素以下
        attachable_id (Union[None, Unset, int]): 添付対象ID
        display_priority (Union[Unset, int]): 表示優先度

            優先度が高いものから順に表示される。
    """

    name: File
    attachable_id: Union[None, Unset, int] = UNSET
    display_priority: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name.to_tuple()

        attachable_id: Union[None, Unset, int]
        if isinstance(self.attachable_id, Unset):
            attachable_id = UNSET
        else:
            attachable_id = self.attachable_id

        display_priority = self.display_priority

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if attachable_id is not UNSET:
            field_dict["attachable_id"] = attachable_id
        if display_priority is not UNSET:
            field_dict["display_priority"] = display_priority

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", self.name.to_tuple()))

        if not isinstance(self.attachable_id, Unset):
            if isinstance(self.attachable_id, int):
                files.append(("attachable_id", (None, str(self.attachable_id).encode(), "text/plain")))
            else:
                files.append(("attachable_id", (None, str(self.attachable_id).encode(), "text/plain")))

        if not isinstance(self.display_priority, Unset):
            files.append(("display_priority", (None, str(self.display_priority).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = File(payload=BytesIO(d.pop("name")))

        def _parse_attachable_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        attachable_id = _parse_attachable_id(d.pop("attachable_id", UNSET))

        display_priority = d.pop("display_priority", UNSET)

        user_upload_post_request = cls(
            name=name,
            attachable_id=attachable_id,
            display_priority=display_priority,
        )

        return user_upload_post_request
