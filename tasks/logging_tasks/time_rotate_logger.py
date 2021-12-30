"""
Настроить логгирование с модулем logging.

Настроить формат вывода.
Настроить, чтобы вывод шел в файл и в консоль.
Настроить ротацию файла лога по времени (полночь).
"""

import logging
from logging.handlers import TimedRotatingFileHandler

mylogs = logging.getLogger(__name__)
mylogs.setLevel(logging.INFO)
file = TimedRotatingFileHandler("log.log", when='midnight')
fileformat = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s", datefmt="%H:%M:%S")
file.setFormatter(fileformat)
mylogs.addHandler(file)
stream = logging.StreamHandler()
streamformat = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s", datefmt="%H:%M:%S")
stream.setFormatter(streamformat)
mylogs.addHandler(stream)


if __name__ == '__main__':
    mylogs.info('все гуд')
    mylogs.error('ошибка')
