# datetime_fun.py
# convert computer time into human readable format
# input: dd.mm.yyyy hh:mm
'''
date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"
# NB: words "hour" and "minute" are used only when time is 01:mm (1 hour) or hh:01 (1 minute).
# In other cases it should be used "hours" and "minutes".
'''
import datetime

def date_time(datestr: str) -> str:
    d, t = datestr.split()

    day, month, year = (int(i.lstrip('0')) for i in d.split('.'))
    hour, minute = (j.lstrip('0') for j in t.split(':'))
    hour = int(hour) if hour != '' else 0
    minute = int(minute) if minute != '' else 0
    dateobj = datetime.datetime(year, month, day, hour, minute)

    hours = 'hour' if hour == 1 else 'hours'
    minutes = 'minute' if minute == 1 else 'minutes'
    monthname = dateobj.strftime('%B')

    return f'{day} {monthname} {year} year {hour} {hours} {minute} {minutes}'

assert date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
assert date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
assert date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"
assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"

print("Coding complete? Click 'Check' to earn cool rewards!")
