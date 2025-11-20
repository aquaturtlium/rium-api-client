import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="LogPostRequest")


@_attrs_define
class LogPostRequest:
    """計測データ POSTリクエストスキーマ

    Attributes:
        time (datetime.datetime): 計測時刻（タイムゾーンは常にJST扱い）
        value (float): 計測値
        sensor_source_id (int): センサソースID
        loggable_id (int): 記録対象ID
    """

    time: datetime.datetime
    value: float
    sensor_source_id: int
    loggable_id: int

    def to_dict(self) -> dict[str, Any]:
        time = self.time.isoformat()

        value = self.value

        sensor_source_id = self.sensor_source_id

        loggable_id = self.loggable_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "time": time,
                "value": value,
                "sensor_source_id": sensor_source_id,
                "loggable_id": loggable_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = isoparse(d.pop("time"))

        value = d.pop("value")

        sensor_source_id = d.pop("sensor_source_id")

        loggable_id = d.pop("loggable_id")

        log_post_request = cls(
            time=time,
            value=value,
            sensor_source_id=sensor_source_id,
            loggable_id=loggable_id,
        )

        return log_post_request
