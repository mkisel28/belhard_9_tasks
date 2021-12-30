"""
Реализация Haversine formula для Python.
https://en.wikipedia.org/wiki/Haversine_formula

Написать функцию distance, которая будет возвращать расстояние между
точками GPS на карте в метрах.

Функция должна принимать следующие аргументы:
* a_lat - широта первой точки
* a_lon - долгота первой точки
* b_lat - широта второй точки
* b_lon - долгота второй точки

Алгоритм:
1. Посчитать значение каждой координаты в радианах.
Формула: float(value) * pi / 180
2. Вычислить sin и cos радианов широт из п1.
3. Вычислить разницу (delta) радианов долгот из п1.
4. Вычислить sin и cos разницы долгот из п3.
5. Вычислить y = sqrt(pow(b_lat_cos * delta_sin, 2)) + pow(a_lat_cos * b_lat_sin - a_lat_sin * b_lat_cos * delta_cos, 2))
6. Вычислить x = a_lat_sin * b_lat_sin + a_lat_cos * b_lat_cos * delta_cos
7. Вычислить ad = atan2(y, x)
8. Вернуть ad * EARTH_R
"""
import math

# радиус сферы (Земли)
EARTH_R = 6372795


def distance(a_lat: float, a_lon: float, b_lat: float, b_lon: float):
    a_lat_rad = a_lat * math.pi / 180
    a_lon_rad = a_lon * math.pi / 180
    b_lat_rad = b_lat * math.pi / 180
    b_lon_rad = b_lon * math.pi / 180
    sin_a_lat_rad = math.sin(a_lat_rad)
    cos_a_lat_rad = math.cos(a_lat_rad)
    sin_b_lat_rad = math.sin(b_lat_rad)
    cos_b_lat_rad = math.cos(b_lat_rad)
    delta_lon = b_lon_rad - a_lon_rad
    sin_delta_lon = math.sin(delta_lon)
    cos_delta_lon = math.cos(delta_lon)
    y = math.sqrt((math.pow(cos_b_lat_rad * sin_delta_lon, 2)) + math.pow(cos_a_lat_rad * sin_b_lat_rad - sin_a_lat_rad * cos_b_lat_rad * cos_delta_lon, 2))
    x = sin_a_lat_rad * sin_b_lat_rad + cos_a_lat_rad * cos_b_lat_rad * cos_delta_lon
    ad = math.atan2(y, x)
    return ad * EARTH_R


if __name__ == '__main__':
    print(distance(53.985, 45.764, 34.876, 90.876))
