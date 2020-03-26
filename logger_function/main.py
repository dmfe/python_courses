import time
from logger import write_log

for count in range(1, 6):
    write_log(f'This is message number {count}')
    time.sleep(1)
