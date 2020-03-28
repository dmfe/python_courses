from datetime import datetime as dt

def format_cur_ts(format_pattern='%Y-%m-%d %H:%M:%S'):
    return dt.now().strftime(format_pattern)
