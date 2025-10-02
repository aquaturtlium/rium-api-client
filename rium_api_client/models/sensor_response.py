from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sensor import Sensor


T = TypeVar("T", bound="SensorResponse")


@_attrs_define
class SensorResponse:
    """センサレスポンススキーマ

    Attributes:
        success (bool): 実行結果
        data (Sensor): **センサ** 計測データを記録するためのデバイス情報
    """

    success: bool
    data: "Sensor"

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "success": success,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sensor import Sensor

        d = dict(src_dict)
        success = d.pop("success")

        data = Sensor.from_dict(d.pop("data"))

        sensor_response = cls(
            success=success,
            data=data,
        )

        return sensor_response
