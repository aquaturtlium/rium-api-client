import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Loggable")


@_attrs_define
class Loggable:
    """**記録対象** 飼育記録・計測データの記録対象（飼育生体または飼育環境）

    Attributes:
        id (Union[Unset, int]): 記録対象ID
        name (Union[Unset, str]): 記録対象名称
        description (Union[Unset, str]): 記録対象詳細
        created (Union[Unset, datetime.datetime]): 作成日時（タイムゾーンは常にJST扱い）
        modified (Union[Unset, datetime.datetime]): 更新日時（タイムゾーンは常にJST扱い）
        user_id (Union[Unset, UUID]): ユーザID
        attachable_id (Union[Unset, int]): 添付対象ID
        images (Union[Unset, list[str]]): アップロードファイルURL配列
        taxon (Union[None, Unset, str]): 生物分類名
        genre (Union[None, Unset, str]): ジャンル名
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    modified: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, UUID] = UNSET
    attachable_id: Union[Unset, int] = UNSET
    images: Union[Unset, list[str]] = UNSET
    taxon: Union[None, Unset, str] = UNSET
    genre: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        modified: Union[Unset, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

        user_id: Union[Unset, str] = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        attachable_id = self.attachable_id

        images: Union[Unset, list[str]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images

        taxon: Union[None, Unset, str]
        if isinstance(self.taxon, Unset):
            taxon = UNSET
        else:
            taxon = self.taxon

        genre: Union[None, Unset, str]
        if isinstance(self.genre, Unset):
            genre = UNSET
        else:
            genre = self.genre

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if attachable_id is not UNSET:
            field_dict["attachable_id"] = attachable_id
        if images is not UNSET:
            field_dict["images"] = images
        if taxon is not UNSET:
            field_dict["taxon"] = taxon
        if genre is not UNSET:
            field_dict["genre"] = genre

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _modified = d.pop("modified", UNSET)
        modified: Union[Unset, datetime.datetime]
        if isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = isoparse(_modified)

        _user_id = d.pop("user_id", UNSET)
        user_id: Union[Unset, UUID]
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        attachable_id = d.pop("attachable_id", UNSET)

        images = cast(list[str], d.pop("images", UNSET))

        def _parse_taxon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        taxon = _parse_taxon(d.pop("taxon", UNSET))

        def _parse_genre(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        genre = _parse_genre(d.pop("genre", UNSET))

        loggable = cls(
            id=id,
            name=name,
            description=description,
            created=created,
            modified=modified,
            user_id=user_id,
            attachable_id=attachable_id,
            images=images,
            taxon=taxon,
            genre=genre,
        )

        return loggable
