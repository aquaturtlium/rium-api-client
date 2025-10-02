from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUpload")


@_attrs_define
class UserUpload:
    """**アップロードファイル** アップロードしたファイルのメタデータ

    Attributes:
        id (Union[Unset, int]): アップロードファイルID
        name (Union[Unset, str]): アップロードファイル名
        type_ (Union[Unset, str]): アップロードファイル種別
        size (Union[Unset, int]): アップロードファイルサイズ（Byte）
        ext (Union[Unset, str]): アップロードファイル拡張子
        user_id (Union[Unset, UUID]): ユーザID
        attachable_id (Union[None, Unset, int]): 添付対象ID
        display_priority (Union[Unset, int]): 表示優先度

            優先度が高いものから順に表示される。
        url (Union[Unset, str]): アップロードファイルURL

            画像サイズ変更なしのアップロードファイルに対するURLを示す。なお、ファイル名に対して以下のプレフィックスを付与したリサイズ画像も使用可能となる。ただし、元画像のサイズがリサイズ後の画像サイズよりも小さい場合は、元画像のサイ
            ズが維持される。
            - `large-` : 長辺1200px（アスペクト比維持）
            - `medium-` : 長辺768px（アスペクト比維持）
            - `small-` : 長辺240px（アスペクト比維持）
            - `rectangle-` : 768x512px
            - `square-` : 110x110px
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    ext: Union[Unset, str] = UNSET
    user_id: Union[Unset, UUID] = UNSET
    attachable_id: Union[None, Unset, int] = UNSET
    display_priority: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        size = self.size

        ext = self.ext

        user_id: Union[Unset, str] = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        attachable_id: Union[None, Unset, int]
        if isinstance(self.attachable_id, Unset):
            attachable_id = UNSET
        else:
            attachable_id = self.attachable_id

        display_priority = self.display_priority

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if size is not UNSET:
            field_dict["size"] = size
        if ext is not UNSET:
            field_dict["ext"] = ext
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if attachable_id is not UNSET:
            field_dict["attachable_id"] = attachable_id
        if display_priority is not UNSET:
            field_dict["display_priority"] = display_priority
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        size = d.pop("size", UNSET)

        ext = d.pop("ext", UNSET)

        _user_id = d.pop("user_id", UNSET)
        user_id: Union[Unset, UUID]
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        def _parse_attachable_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        attachable_id = _parse_attachable_id(d.pop("attachable_id", UNSET))

        display_priority = d.pop("display_priority", UNSET)

        url = d.pop("url", UNSET)

        user_upload = cls(
            id=id,
            name=name,
            type_=type_,
            size=size,
            ext=ext,
            user_id=user_id,
            attachable_id=attachable_id,
            display_priority=display_priority,
            url=url,
        )

        return user_upload
