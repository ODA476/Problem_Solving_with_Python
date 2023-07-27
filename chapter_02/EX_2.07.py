"""
**2.7 (Find the number of years and days) Write a program that prompts the user to
enter the minutes (e.g., 1 billion), and displays the number of years and days for
the minutes. For simplicity, assume a year has 365 days.
"""

# Enter the number of minutes.
minutes = eval(input('Enter the number of minutes: '))

# convert to years. (365 * 24 * 60 = 525600 minutes per year.)
years = minutes // 525600

# convert to day. (one day has 1440 minutes)
# minutes % 525600 = the remaining minutes that make up less than a year
days = (minutes % 525600) // 1440

# display the result.
print(f'{minutes} minutes is approximately {years} years and {days} days.')
