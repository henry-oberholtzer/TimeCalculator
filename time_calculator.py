import re
import math


def add_time(start, duration, day=None):
    # get numbers from inputs
    nums = re.compile(r'\d{1,}')
    am_pm = re.search(r'AM|PM', start)[0]
    start_mins = int((start_list := nums.findall(start))[0]) * 60 + int(start_list[1])
    duration_mins = int((duration_list := nums.findall(duration))[0]) * 60 + int(duration_list[1])
    
    # get the total minutes
    if am_pm != 'AM':
        start_mins += 12 * 60
    sum_mins = start_mins + duration_mins

    # get the numbers to display
    hours = math.trunc(sum_mins / 60)
    mins = sum_mins % 60
    days = math.trunc(hours / 24)
    
    # set AM or PM
    if math.trunc(hours / 12) % 2 != 0:
        am_pm = 'PM'
        days += .5
    else:
        am_pm = 'AM'
    
    # calculaste days later
    days_later = ''
    if days == 1:
        days_later = ' (next day)'
    elif days > 1:
        days_later = f' ({days} days later)'

    # print formatting
    hours_print = int(hours - 24 * days)
    if hours_print == 0:
        hours_print += 12

    return f'{hours_print}:{str(mins).zfill(2)} {am_pm}{days_later}'
