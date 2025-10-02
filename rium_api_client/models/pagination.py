from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """ページネーション情報

    Attributes:
        page_count (int): 総ページ数
        current_page (int): 現在のページ番号
        has_next_page (bool): 次ページの有無
        has_prev_page (bool): 前ページの有無
        count (int): 総アイテム数
        limit (Union[None, int]): 1ページあたりアイテム数

            クエリパラメータ`limit`で指定されない場合は`null`を返しアイテム数は20件となる。
    """

    page_count: int
    current_page: int
    has_next_page: bool
    has_prev_page: bool
    count: int
    limit: Union[None, int]

    def to_dict(self) -> dict[str, Any]:
        page_count = self.page_count

        current_page = self.current_page

        has_next_page = self.has_next_page

        has_prev_page = self.has_prev_page

        count = self.count

        limit: Union[None, int]
        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "page_count": page_count,
                "current_page": current_page,
                "has_next_page": has_next_page,
                "has_prev_page": has_prev_page,
                "count": count,
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_count = d.pop("page_count")

        current_page = d.pop("current_page")

        has_next_page = d.pop("has_next_page")

        has_prev_page = d.pop("has_prev_page")

        count = d.pop("count")

        def _parse_limit(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        limit = _parse_limit(d.pop("limit"))

        pagination = cls(
            page_count=page_count,
            current_page=current_page,
            has_next_page=has_next_page,
            has_prev_page=has_prev_page,
            count=count,
            limit=limit,
        )

        return pagination
