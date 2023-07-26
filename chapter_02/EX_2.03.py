"""
2.3 (Convert feet into meters) Write a program that reads a number in feet, converts it
to meters, and displays the result. One foot is 0.305 meters.
    meter = feet * 0.305
"""

# Enter the value by feet
feet = eval(input('Enter a value for feet: '))

# convert feet into meters
meter = feet * 0.305

# display the result
print(f'{feet} feet is {meter} meters')
