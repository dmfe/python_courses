from datetime import datetime as dt

def cur_datetime():
    format_str = "%Y-%m-%d %H:%M:%S"
    return dt.now().strftime(format_str)

def write_log(log_str=''):
    with open('log.data', 'a') as log_file:
        log_file.write(f'[{cur_datetime()}] {log_str}\n')
