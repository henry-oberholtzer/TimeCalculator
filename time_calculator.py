import re


def add_time(start, duration, day=None):
    nums = re.compile(r'\d{1,}')
    start_hours = int((start_list := nums.findall(start))[0])
    start_mins = int(start_list[1])
    am_pm = re.search(r'AM|PM', start)[0]
    duration_hours = int((duration_list := nums.findall(duration))[0])
    duration_mins = int(duration_list[1])

    sum_mins = start_mins + duration_mins
    
    sum_hours = start_hours + duration_hours + round(60 / sum_mins % 1)

    if sum_hours / 12 > 1:
        if am_pm == 'AM':
            am_pm = 'PM'
        else:
            am_pm = 'AM'


    return f'{sum_hours - 12 * round(sum_hours / 12)}:{str(sum_mins % 60).zfill(2)} {am_pm}'
