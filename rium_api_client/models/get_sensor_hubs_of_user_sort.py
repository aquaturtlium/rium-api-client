from enum import Enum


class GetSensorHubsOfUserSort(str, Enum):
    ID = "id"
    IS_AUTO = "is_auto"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
