from datetime import datetime as dt
from enum import Enum


class Severity(Enum):
    ERROR = {'str': 'ERROR', 'weight': 5}
    INFO = {'str': 'INFO', 'weight': 10}


DEFAULT_LOG_FILE_NAME = 'dummy.log'
DEFAULT_LOG_LEVEL = Severity.INFO


class Logger:

    def __init__(self, file_name=DEFAULT_LOG_FILE_NAME, level=DEFAULT_LOG_LEVEL):
        self.log_file_name = file_name
        self.log_level = level

    def __enter__(self):
        self.log_file = open(self.log_file_name, 'a')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.log_file.close()
        if exc_val:
            raise

    def info(self, msg=''):
        self.__log(Severity.INFO, msg)

    def error(self, msg=''):
        self.__log(Severity.ERROR, msg)

    def __log(self, severity, msg):
        if not self.log_file:
            raise ValueError('Log file is not opened.')

        if severity.value['weight'] <= self.log_level.value['weight']:
            self.log_file.write(f'{self.__cur_ts()} [{severity.value["str"]}] {msg}\n')

    def __cur_ts(self):
        format_pattern = '%Y-%m-%d %H:%M:%S'
        return dt.now().strftime(format_pattern)
