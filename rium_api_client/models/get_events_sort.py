from enum import Enum


class GetEventsSort(str, Enum):
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
