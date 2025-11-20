import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eventive_tag_post_request import EventiveTagPostRequest
    from ..models.related_ids import RelatedIds


T = TypeVar("T", bound="EventPostRequest")


@_attrs_define
class EventPostRequest:
    """飼育記録 POSTリクエストスキーマ

    Attributes:
        time (datetime.datetime): 計測時刻（タイムゾーンは常にJST扱い）
        loggable_id (int): 記録対象ID
        description (Union[Unset, str]): 記録内容
        eventive_tags (Union['RelatedIds', Unset, list['EventiveTagPostRequest']]): 関連飼育記録タグ指定情報
    """

    time: datetime.datetime
    loggable_id: int
    description: Union[Unset, str] = UNSET
    eventive_tags: Union["RelatedIds", Unset, list["EventiveTagPostRequest"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.related_ids import RelatedIds

        time = self.time.isoformat()

        loggable_id = self.loggable_id

        description = self.description

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

        field_dict.update(
            {
                "time": time,
                "loggable_id": loggable_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if eventive_tags is not UNSET:
            field_dict["eventive_tags"] = eventive_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eventive_tag_post_request import EventiveTagPostRequest
        from ..models.related_ids import RelatedIds

        d = dict(src_dict)
        time = isoparse(d.pop("time"))

        loggable_id = d.pop("loggable_id")

        description = d.pop("description", UNSET)

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

        event_post_request = cls(
            time=time,
            loggable_id=loggable_id,
            description=description,
            eventive_tags=eventive_tags,
        )

        return event_post_request
