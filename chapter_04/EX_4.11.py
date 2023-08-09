"""
*4.11 (Find the number of days in a month) Write a program that prompts the user to
enter the month and year and displays the number of days in the month. For example, if the user entered month 2 and year 2000,
the program should display that February 2000 has 29 days.
If the user entered month 3 and year 2005, the program should display that March 2005 has 31 days.
"""

# Enter the month and year
month, year = eval(input('Enter the month and year: ').strip())

# check if year is leap year
is_leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# determine month's name and number of days in this month
if month == 1:
    month_name = 'January'
    day_per_month = 31
elif month == 2:
    month_name = 'February'
    if is_leap_year:
        day_per_month = 29
    else:
        day_per_month = 28
elif month == 3:
    month_name = 'March'
    day_per_month = 31
elif month == 4:
    month_name = 'April'
    day_per_month = 30
elif month == 5:
    month_name = 'May'
    day_per_month = 31
elif month == 6:
    month_name = 'June'
    day_per_month = 30
elif month == 7:
    month_name = 'July'
    day_per_month = 31
elif month == 8:
    month_name = 'August'
    day_per_month = 31
elif month == 9:
    month_name = 'September'
    day_per_month = 30
elif month == 10:
    month_name = 'October'
    day_per_month = 31
elif month == 11:
    month_name = 'November'
    day_per_month = 30
elif month == 12:
    month_name = 'December'
    day_per_month = 31

# display the result
print(f'{month_name} {year} has {day_per_month} days')
