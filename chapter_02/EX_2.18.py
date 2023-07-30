"""
*2.18 (Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays the
current time in GMT. Revise the program so that it prompts the user to enter the
time zone in hours away from (offset to) GMT and displays the time in the specified time zone
"""

# this code same the listing 2.7 and some addition

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

# some addition
# Enter the time zone offset to GMT
offset = eval(input('Enter the time zone offset to GMT: '))
currentHour = currentHour + offset

# display the current time
print(f'The current time is {currentHour}:{currentMinute}:{currentSecond}')
