"""
*4.20 (Science: wind-chill temperature) Exercise 2.9 gives a formula to compute the
wind-chill temperature. The formula is valid for temperatures in the range
between and 41°F and for wind speed greater than or equal to 2. Write a
program that prompts the user to enter a temperature and a wind speed.
The program displays the wind-chill temperature if the input is valid; otherwise,
it displays a message indicating whether the temperature and/or wind speed is invalid.
"""

# Enter the temperature in Fahrenheit between -58 and 41
ta = eval(input('Enter the temperature in Fahrenheit between -58 and 41: '))

# Enter the wind speed in miles per hour
v = eval(input('Enter the wind speed in miles per hour: '))

# display the result
if -58 < ta < 41 and v >= 2:
    # calculate the wind chill index
    twc = 35.74 + 0.6215 * ta - 35.75 * v ** 0.16 + 0.4275 * ta * v ** 0.16
    # display result
    print('The wind chill index is ', twc)
else:
    print('the temperature and/or wind speed is invalid.')
