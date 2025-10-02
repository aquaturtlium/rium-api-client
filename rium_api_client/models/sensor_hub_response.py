from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sensor_hub import SensorHub


T = TypeVar("T", bound="SensorHubResponse")


@_attrs_define
class SensorHubResponse:
    """センサハブレスポンススキーマ

    Attributes:
        success (bool): 実行結果
        data (SensorHub): **センサハブ** ネットワーク接続時等に複数のセンサ情報をまとめるハブデバイス情報
    """

    success: bool
    data: "SensorHub"

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
        from ..models.sensor_hub import SensorHub

        d = dict(src_dict)
        success = d.pop("success")

        data = SensorHub.from_dict(d.pop("data"))

        sensor_hub_response = cls(
            success=success,
            data=data,
        )

        return sensor_hub_response
