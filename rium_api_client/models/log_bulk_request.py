import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_value import LogValue


T = TypeVar("T", bound="LogBulkRequest")


@_attrs_define
class LogBulkRequest:
    """一括登録時計測データリクエストスキーマ

    Attributes:
        time (datetime.datetime): 計測時刻
        value (LogValue):
        sensor_source_id (int): センサソースID
        loggable_id (Union[Unset, int]): 記録対象ID
    """

    time: datetime.datetime
    value: "LogValue"
    sensor_source_id: int
    loggable_id: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        time = self.time.isoformat()

        value = self.value.to_dict()

        sensor_source_id = self.sensor_source_id

        loggable_id = self.loggable_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "time": time,
                "value": value,
                "sensor_source_id": sensor_source_id,
            }
        )
        if loggable_id is not UNSET:
            field_dict["loggable_id"] = loggable_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_value import LogValue

        d = dict(src_dict)
        time = isoparse(d.pop("time"))

        value = LogValue.from_dict(d.pop("value"))

        sensor_source_id = d.pop("sensor_source_id")

        loggable_id = d.pop("loggable_id", UNSET)

        log_bulk_request = cls(
            time=time,
            value=value,
            sensor_source_id=sensor_source_id,
            loggable_id=loggable_id,
        )

        return log_bulk_request
