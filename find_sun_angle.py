# find_sun_angle.py
'''
Your task is to find the angle of the sun above the horizon knowing the time of the day. 
Input data: 
The sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. 
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees. 
6:00 PM is the time of the sunset so the angle is 180 degrees. 
If the input will be the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".
Precondition: 00:00 <= time <= 23:59
'''
from typing import Union

def sun_angle(time: str) -> Union[int, str]:
    # convert 24 hour time to minutes
    time_tuple = tuple(time.split(':'))
    time = int(time_tuple[0]) * 60 + int(time_tuple[1])
    # > 1800 or < 0600
    if int(time) > 1080 or int(time) < 360:
        return "I don't see the sun!"
    else:
        # 0600 is 360 minutes and each degree is 0.25
        return (time - 360) * 0.25

assert sun_angle("19:00") == "I don't see the sun!"
assert sun_angle("06:00") == 0
assert sun_angle("09:00") == 45
assert sun_angle("12:00") == 90
assert sun_angle("15:00") == 135
assert sun_angle("18:00") == 180

