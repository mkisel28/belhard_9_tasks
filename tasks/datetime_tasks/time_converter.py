"""
Написать функцию convert_date, которая будет конвертировать время
из одной временной зоны в другую.

Функция должна принимать 3 аргумента: timestamp, current_zone, new_zone.

Функция должна возвращать время в новой временной зоне.
"""
from datetime import datetime
import pytz


def convert_date(timestamp, current_zone, new_zone):
    current_zone_time = datetime.fromtimestamp(timestamp)
    current_zone_object = pytz.timezone(current_zone)
    new_zone_object = pytz.timezone(new_zone)
    localized_timestamp = current_zone_object.localize(current_zone_time)
    return localized_timestamp.astimezone(new_zone_object)


if __name__ == '__main__':
    print(convert_date(1585222256, "US/Eastern", "US/Pacific"))
