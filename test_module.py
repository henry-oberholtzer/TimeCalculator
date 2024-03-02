import pytest 
from time_calculator import add_time


test_cases = [
    pytest.param(
        "3:30 PM", "2:12",
        "5:42 PM",
        'Expected calling "add_time()" with "3:30 PM", "2:12" to return "5:42 PM"',
        id="test_same_period"
    ),
    pytest.param(
        "11:55 AM", "3:12",
        "3:07 PM",
        'Expected calling "add_time()" with "11:55 AM", "3:12" to return "3:07 PM"',
        id = "different_period"
    ),
    pytest.param(
        "9:15 PM", "5:30",
        "2:45 AM (next day)",
        'Expected time to end with "(next day)" when it is the next day.',
        id="test_next_day"
    ),
    pytest.param(
        "11:40 AM", "0:25",
        "12:05 PM",
        'Expected period to change from AM to PM at 12:00',
        id="test_period_change_at_twelve"
    ),
    pytest.param(
        "2:59 AM", "24:00",
        "2:59 AM (next day)",
        'Expected calling "add_time()" with "2:59 AM", "24:00" to return "2:59 AM"',
        id="test_twenty_four"
    ),
    pytest.param(
        "11:59 PM", "24:05",
        "12:04 AM (2 days later)",
        'Expected calling "add_time()" with "11:59 PM", "24:05" to return "12:04 AM (2 days later)"',
        id="test_two_days_later"
    ),
    pytest.param(
        "8:16 PM", "466:02",
        "6:18 AM (20 days later)",
        'Expected calling "add_time()" with "8:16 PM", "466:02" to return "6:18 AM (20 days later)"',
        id="test_high_duration"
    ),
    pytest.param(
        "5:01 AM", "0:00",
        "5:01 AM",
        'Expected adding 0:00 to return initial time.',
        id="test_no_change"
    ),

]

#     def test_same_period_with_day(self):
#         actual = add_time("3:30 PM", "2:12", "Monday")
#         expected = "5:42 PM, Monday"
#         self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12", "Monday" to return "5:42 PM, Monday"')

#     def test_twenty_four_with_day(self):
#         actual = add_time("2:59 AM", "24:00", "saturDay")
#         expected = "2:59 AM, Sunday (next day)"
#         self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00", "saturDay" to return "2:59 AM, Sunday (next day)"')

#     def test_two_days_later_with_day(self):
#         actual = add_time("11:59 PM", "24:05", "Wednesday")
#         expected = "12:04 AM, Friday (2 days later)"
#         self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05", "Wednesday" to return "12:04 AM, Friday (2 days later)"')

#     def test_high_duration_with_day(self):
#         actual = add_time("8:16 PM", "466:02", "tuesday")
#         expected = "6:18 AM, Monday (20 days later)"
#         self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02", "tuesday" to return "6:18 AM, Monday (20 days later)"')

@pytest.mark.parametrize('start,duration,expected_output,fail_message', test_cases)
def test_template(start, duration, expected_output, fail_message):
    actual = add_time(start, duration)
    assert actual == expected_output, fail_message
