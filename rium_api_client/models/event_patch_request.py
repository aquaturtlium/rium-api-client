import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eventive_tag_post_request import EventiveTagPostRequest
    from ..models.related_ids import RelatedIds


T = TypeVar("T", bound="EventPatchRequest")


@_attrs_define
class EventPatchRequest:
    """飼育記録 PATCHリクエストスキーマ

    Attributes:
        time (Union[Unset, datetime.datetime]): 計測時刻
        description (Union[Unset, str]): 記録内容
        loggable_id (Union[Unset, int]): 記録対象ID
        eventive_tags (Union['RelatedIds', Unset, list['EventiveTagPostRequest']]): 関連飼育記録タグ指定情報
    """

    time: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    loggable_id: Union[Unset, int] = UNSET
    eventive_tags: Union["RelatedIds", Unset, list["EventiveTagPostRequest"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.related_ids import RelatedIds

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        description = self.description

        loggable_id = self.loggable_id

        eventive_tags: Union[Unset, dict[str, Any], list[dict[str, Any]]]
        if isinstance(self.eventive_tags, Unset):
            eventive_tags = UNSET
        elif isinstance(self.eventive_tags, RelatedIds):
            eventive_tags = self.eventive_tags.to_dict()
        else:
            eventive_tags = []
            for componentsschemas_eventive_tag_relation_type_1_item_data in self.eventive_tags:
                componentsschemas_eventive_tag_relation_type_1_item = (
                    componentsschemas_eventive_tag_relation_type_1_item_data.to_dict()
                )
                eventive_tags.append(componentsschemas_eventive_tag_relation_type_1_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if description is not UNSET:
            field_dict["description"] = description
        if loggable_id is not UNSET:
            field_dict["loggable_id"] = loggable_id
        if eventive_tags is not UNSET:
            field_dict["eventive_tags"] = eventive_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eventive_tag_post_request import EventiveTagPostRequest
        from ..models.related_ids import RelatedIds

        d = dict(src_dict)
        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        description = d.pop("description", UNSET)

        loggable_id = d.pop("loggable_id", UNSET)

        def _parse_eventive_tags(data: object) -> Union["RelatedIds", Unset, list["EventiveTagPostRequest"]]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_eventive_tag_relation_type_0 = RelatedIds.from_dict(data)

                return componentsschemas_eventive_tag_relation_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            componentsschemas_eventive_tag_relation_type_1 = []
            _componentsschemas_eventive_tag_relation_type_1 = data
            for (
                componentsschemas_eventive_tag_relation_type_1_item_data
            ) in _componentsschemas_eventive_tag_relation_type_1:
                componentsschemas_eventive_tag_relation_type_1_item = EventiveTagPostRequest.from_dict(
                    componentsschemas_eventive_tag_relation_type_1_item_data
                )

                componentsschemas_eventive_tag_relation_type_1.append(
                    componentsschemas_eventive_tag_relation_type_1_item
                )

            return componentsschemas_eventive_tag_relation_type_1

        eventive_tags = _parse_eventive_tags(d.pop("eventive_tags", UNSET))

        event_patch_request = cls(
            time=time,
            description=description,
            loggable_id=loggable_id,
            eventive_tags=eventive_tags,
        )

        return event_patch_request
