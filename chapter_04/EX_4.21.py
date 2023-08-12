"""
**4.21 (Science: day of the week) Zeller’s congruence is an algorithm developed by
Christian Zeller to calculate the day of the week. The formula is
    h = (q + floor(26 * (m + 1) / 10) + k + floor(k / 4) + floor(j / 4) + (5 * j)) % 7
where
■ h is the day of the week (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday,
4: Wednesday, 5: Thursday, 6: Friday).
■ q is the day of the month.
■ m is the month (3: March, 4: April, ..., 12: December). January and February are
counted as months 13 and 14 of the previous year.
■ j is the century (i.e., ).
■ k is the year of the century (i.e., year % 100).

Write a program that prompts the user to enter a year, month, and day of the
month, and then it displays the name of the day of the week.
"""
import math

# Enter year
year = int(input('Enter year: (e.g., 2008): ').strip())

# Enter month
m = int(input('Enter month: 1-12: ').strip())

# January and February are
# counted as months 13 and 14 of the previous year (year - 1 >> to compute a previous year).
if m == 1:
    m = 13
    year -= 1
elif m == 2:
    m = 14
    year -= 1

# Enter the day of the month
q = int(input('Enter the day of the month: 1-31: ').strip())

# compute k
k = year % 100

# compute j
j = math.floor(year / 100)

# compute h here, I guess, We can't use {math.floor()}, because (//) operation in python default return floor
# function. (be sure from this advice)
h = (q + math.floor(26 * (m + 1) / 10) + k + math.floor(k / 4) + math.floor(j / 4) + (5 * j)) % 7

# choose the days' name
if h == 0:
    day_name = 'Saturday'
elif h == 1:
    day_name = 'Sunday'
elif h == 2:
    day_name = 'Monday'
elif h == 3:
    day_name = 'Tuesday'
elif h == 4:
    day_name = 'Wednesday'
elif h == 5:
    day_name = 'Thursday'
else:
    day_name = 'Friday'

# display result
print(f'Day of the week is {day_name}')
