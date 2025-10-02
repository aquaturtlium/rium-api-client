from enum import Enum


class GetSensorsOfSensorHubSort(str, Enum):
    ACTIVE = "active"
    ID = "id"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
