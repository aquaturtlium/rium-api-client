from enum import IntEnum


class SensorSourceTypeId(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_900 = 900
    VALUE_999 = 999

    def __str__(self) -> str:
        return str(self.value)
