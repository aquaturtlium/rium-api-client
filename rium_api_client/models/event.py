import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eventive_tag import EventiveTag


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """**飼育記録** 飼育生体・飼育環境に対するテキストベースの記録

    Attributes:
        id (Union[Unset, int]): 飼育記録ID
        time (Union[Unset, datetime.datetime]): 計測時刻（タイムゾーンは常にJST扱い）
        description (Union[Unset, str]): 記録内容
        loggable_id (Union[Unset, int]): 記録対象ID
        attachable_id (Union[Unset, int]): 添付対象ID
        is_uploaded (Union[Unset, bool]): ユーザによる画像のアップロード有無
        eventive_tags (Union[Unset, list['EventiveTag']]): 飼育記録タグ配列
    """

    id: Union[Unset, int] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    loggable_id: Union[Unset, int] = UNSET
    attachable_id: Union[Unset, int] = UNSET
    is_uploaded: Union[Unset, bool] = UNSET
    eventive_tags: Union[Unset, list["EventiveTag"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        description = self.description

        loggable_id = self.loggable_id

        attachable_id = self.attachable_id

        is_uploaded = self.is_uploaded

        eventive_tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eventive_tags, Unset):
            eventive_tags = []
            for eventive_tags_item_data in self.eventive_tags:
                eventive_tags_item = eventive_tags_item_data.to_dict()
                eventive_tags.append(eventive_tags_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if time is not UNSET:
            field_dict["time"] = time
        if description is not UNSET:
            field_dict["description"] = description
        if loggable_id is not UNSET:
            field_dict["loggable_id"] = loggable_id
        if attachable_id is not UNSET:
            field_dict["attachable_id"] = attachable_id
        if is_uploaded is not UNSET:
            field_dict["is_uploaded"] = is_uploaded
        if eventive_tags is not UNSET:
            field_dict["eventive_tags"] = eventive_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eventive_tag import EventiveTag

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        description = d.pop("description", UNSET)

        loggable_id = d.pop("loggable_id", UNSET)

        attachable_id = d.pop("attachable_id", UNSET)

        is_uploaded = d.pop("is_uploaded", UNSET)

        eventive_tags = []
        _eventive_tags = d.pop("eventive_tags", UNSET)
        for eventive_tags_item_data in _eventive_tags or []:
            eventive_tags_item = EventiveTag.from_dict(eventive_tags_item_data)

            eventive_tags.append(eventive_tags_item)

        event = cls(
            id=id,
            time=time,
            description=description,
            loggable_id=loggable_id,
            attachable_id=attachable_id,
            is_uploaded=is_uploaded,
            eventive_tags=eventive_tags,
        )

        return event
