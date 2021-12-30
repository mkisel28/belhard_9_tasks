"""
Написать класс FilmTypes, который будет наследоваться от Enum и содержать
константы-названия жанров фильмов.
"""

from enum import Enum


class FilmTypes(Enum):
    COMEDY = 1
    DRAMA = 2
    HORROR = 3
    FANTASY = 4
    WESTERN = 5
