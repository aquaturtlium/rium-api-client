from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_errors import ErrorErrors


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """エラー

    Attributes:
        code (int): HTTPステータスコード
        message (str): エラーメッセージ
        url (Union[Unset, str]): URL
        error_count (Union[Unset, int]): エラー件数
        errors (Union[Unset, ErrorErrors]): エラー詳細
    """

    code: int
    message: str
    url: Union[Unset, str] = UNSET
    error_count: Union[Unset, int] = UNSET
    errors: Union[Unset, "ErrorErrors"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        url = self.url

        error_count = self.error_count

        errors: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if error_count is not UNSET:
            field_dict["errorCount"] = error_count
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_errors import ErrorErrors

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        url = d.pop("url", UNSET)

        error_count = d.pop("errorCount", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: Union[Unset, ErrorErrors]
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = ErrorErrors.from_dict(_errors)

        error = cls(
            code=code,
            message=message,
            url=url,
            error_count=error_count,
            errors=errors,
        )

        error.additional_properties = d
        return error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
