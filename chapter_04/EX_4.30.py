"""
*4.30 (Current time) Revise Programming Exercise 2.18 to display the hour using a 12-
hour clock.
"""

# this EX_2.18 code
# the addition there is at display section

import time

currentTime = time.time()  # Get current time
# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)
# Get the current second
currentSecond = totalSeconds % 60
# Obtain the total minutes
totalMinutes = totalSeconds // 60
# Compute the current minute in the hour
currentMinute = totalMinutes % 60
# Obtain the total hours
totalHours = totalMinutes // 60
# Compute the current hour
currentHour = totalHours % 24

# Enter the time zone offset to GMT
offset = eval(input('Enter the time zone offset to GMT: '))
currentHour = currentHour + offset

# display the current time
if currentHour == 12:
    print(f'The current time is {currentHour}:{currentMinute}:{currentSecond} PM')
elif currentHour > 12:
    print(f'The current time is {currentHour % 12}:{currentMinute}:{currentSecond} PM')
else:
    print(f'The current time is {currentHour}:{currentMinute}:{currentSecond} AM')
