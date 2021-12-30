"""
Написать класс Day, который будет наследоваться от Enum и содержать
константы-названия дней недели на английском языке
"""

from enum import Enum


class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
