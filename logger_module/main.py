from logger import Logger
from logger import loggable
from logger import Severity

# Example with context manager
with Logger() as log:
    for num in range(1, 6):
        if num < 5:
            log.info(f'Info message number {num}')
        else:
            log.error(f'Error message number {num}')

# Examples with decorator
@loggable(file_name='info.log', level=Severity.INFO)
def do_smth_loggable_info():
    print('Do something info')

@loggable(file_name='info.log', level=Severity.INFO)
def do_smth_loggable_info_with_error():
    print('Do something info')
    raise Exception('Something terrible happened! We will all die!')

@loggable(file_name='error.log', level=Severity.ERROR)
def do_smth_loggable_error():
    print('Do something error')
    raise Exception('Something terrible happened! We will all die!')

do_smth_loggable_info()
do_smth_loggable_info_with_error()
do_smth_loggable_error()
