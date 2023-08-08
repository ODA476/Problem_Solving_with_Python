"""
*4.5 (Find future dates) Write a program that prompts the user to enter an integer for
today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
prompt the user to enter the number of days after today for a future day and display the future day of the week.
"""
import sys

# Enter today's day
today = int(input("Enter today's day: ").strip())
# check if today >= 6 __ we will stop the program
if today >= 6:
    sys.exit()

# determine the today's name
if today == 0:
    today_name = 'Sunday'
elif today == 1:
    today_name = 'Monday'
elif today == 2:
    today_name = 'Tuesday'
elif today == 3:
    today_name = 'Wednesday'
elif today == 4:
    today_name = 'Thursday'
elif today == 5:
    today_name = 'Friday'
else:
    today_name = 'Saturday'

# Enter the number of days elapsed since today
number_of_today = int(input('Enter the number of days elapsed since today: ').strip())

# find future dates
future_dates = (number_of_today + today) % 7

# find today's name
if future_dates == 0:
    day_name = 'Sunday'
elif future_dates == 1:
    day_name = 'Monday'
elif future_dates == 2:
    day_name = 'Tuesday'
elif future_dates == 3:
    day_name = 'Wednesday'
elif future_dates == 4:
    day_name = 'Thursday'
elif future_dates == 5:
    day_name = 'Friday'
else:
    day_name = 'Saturday'

# display the result
print(f'Today is {today_name} and the future day is {day_name}')
