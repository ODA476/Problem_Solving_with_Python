"""
1.10 (Average speed) Assume a runner runs 14 kilometers in 45 minutes and 30 seconds.
Write a program that displays the average speed in miles per hour.
(Note that 1 mile is 1.6 kilometers.)
"""

# first, we want to convert all time to hour unit,
# because question require to display the average in mile per (hour).

# 45 * 60 >> convert minutes to seconds
# /3600 >> to convert seconds to hours
hour = ((45 * 60) + 30) / 3600

# second, we must convert distance to miles.
mile = 14 / 1.6

# finally, calculate the average speed by (distance / time)
speed_average = mile / hour

# display the result
# (:.3f) to display only three digit after point
print(f'Speed average = {speed_average:.3f}')

# (Note) In addition, we can calculate average speed by kilometer and (second or minutes), and covert to mile per hour
