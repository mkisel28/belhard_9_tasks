"""
Написать функцию add_to_path, которая будет добавлять директорию, в которой находится
переданный файл (путь к файлу) в sys.path
"""

import sys


def add_to_path(file_path):
    sys.path.append(file_path)
