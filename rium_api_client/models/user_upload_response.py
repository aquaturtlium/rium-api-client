from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.user_upload import UserUpload


T = TypeVar("T", bound="UserUploadResponse")


@_attrs_define
class UserUploadResponse:
    """アップロードファイルレスポンススキーマ

    Attributes:
        success (bool): 実行結果
        data (UserUpload): **アップロードファイル** アップロードしたファイルのメタデータ
    """

    success: bool
    data: "UserUpload"

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
        from ..models.user_upload import UserUpload

        d = dict(src_dict)
        success = d.pop("success")

        data = UserUpload.from_dict(d.pop("data"))

        user_upload_response = cls(
            success=success,
            data=data,
        )

        return user_upload_response
