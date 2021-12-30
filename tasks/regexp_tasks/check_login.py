"""
Написать функцию check_login, которая будет принимать строку и проверять,
что она является логином, который соответствует следующим правилам:
1. Длина от 5 до 20 символов
2. Состоит из букв верхнего и нижнего регистра, цифр, знаков подчеркивания
"""
import re


def check_login(login: str):
    pattern = '[A-Za-z0-9_]{5,20}'
    if re.fullmatch(pattern, login):
        print('Все окей')
    else:
        print('Логин неверный')


if __name__ == '__main__':
    check_login('asdag_2318')
    check_login('sdfsaDy$')
    check_login('sFDVDS')
    check_login('1123')
