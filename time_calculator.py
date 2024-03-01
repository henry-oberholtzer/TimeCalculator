import re


def add_time(start, duration, day=None):
    nums = re.compile(r'\d{1,}')
    start_hours = int((start_list := nums.findall(start))[0])
    start_mins = int(start_list[1])
    start_am_pm = re.search(r'AM|PM', start)[0]
    duration_hours = int((duration_list := nums.findall(duration))[0])
    duration_mins = int(duration_list[1])
    return f'{start_hours + duration_hours}:{start_mins + duration_mins} {start_am_pm}'
