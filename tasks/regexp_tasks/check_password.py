"""
Написать функцию check_password, которая будет принимать строку и проверять,
что она является паролем, который соответствует следующим правилам:
1. Длина от 8 до 40 символов
2. Должен включать букву верхнего регистра
3. Должен включать букву нижнего регистра
4. Должен включать цифру
5. Должен включать символ (из некоторого набора или исключения)

Подсказка:
Понадобится позитивный просмотр вперед (?=чтото)
"""
import re


def check_password(password: str):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,40}$"
    if re.fullmatch(pattern, password):
        print('оК')
    else:
        print('НЕ ОК')


if __name__ == '__main__':
    check_password('Fdf!sdsaS3a')
    check_password('SAD@!')
    check_password('1232346')
    check_password('Aa1!rj')
