# Time Calculator

A script written following the rules set out in the challenge prompt on freeCodeCamp's [Scientific Computing With Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator) course.

# Functionality

- Takes in a start time in the 12-hour clock format (AM or PM)
- A duration indicating hours and minutes
- Optional, a starting day of the week (case insensitive)
- Function should add duration time to the start time and return the result
- If the result will be the next day, it should show `(next day)` after the time
- If the result will be more than one day later show `(n days later)`
- If given the starting day of the week, display the day of the week, after time and before number of days later.

## Examples

```
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

## License

Prompt & boilerplate © freeCodeCamp

Code in `time_calculator.py` © Henry Oberholtzer

Licensed under a GNU GPLv3 license
