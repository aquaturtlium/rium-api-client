from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sensor_source import SensorSource


T = TypeVar("T", bound="SensorSourceResponse")


@_attrs_define
class SensorSourceResponse:
    """センサソースレスポンススキーマ

    Attributes:
        success (bool): 実行結果
        data (SensorSource): **センサソース** センサが取得できる信号の情報
    """

    success: bool
    data: "SensorSource"

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
        from ..models.sensor_source import SensorSource

        d = dict(src_dict)
        success = d.pop("success")

        data = SensorSource.from_dict(d.pop("data"))

        sensor_source_response = cls(
            success=success,
            data=data,
        )

        return sensor_source_response
