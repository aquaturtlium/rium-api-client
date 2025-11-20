import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Log")


@_attrs_define
class Log:
    """**計測データ** 飼育生体・飼育環境に対する数値データ

    Attributes:
        time (Union[Unset, datetime.datetime]): 計測時刻（タイムゾーンは常にJST扱い）
        value (Union[Unset, float]): 計測値
        sensor_source_id (Union[Unset, int]): センサソースID
        loggable_id (Union[Unset, int]): 記録対象ID
    """

    time: Union[Unset, datetime.datetime] = UNSET
    value: Union[Unset, float] = UNSET
    sensor_source_id: Union[Unset, int] = UNSET
    loggable_id: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        value = self.value

        sensor_source_id = self.sensor_source_id

        loggable_id = self.loggable_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if value is not UNSET:
            field_dict["value"] = value
        if sensor_source_id is not UNSET:
            field_dict["sensor_source_id"] = sensor_source_id
        if loggable_id is not UNSET:
            field_dict["loggable_id"] = loggable_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        value = d.pop("value", UNSET)

        sensor_source_id = d.pop("sensor_source_id", UNSET)

        loggable_id = d.pop("loggable_id", UNSET)

        log = cls(
            time=time,
            value=value,
            sensor_source_id=sensor_source_id,
            loggable_id=loggable_id,
        )

        return log
