"""
2.1 (Convert Celsius to Fahrenheit) Write a program that reads a Celsius degree from
the console and converts it to Fahrenheit and displays the result. The formula for
the conversion is as follows:
    fahrenheit = (9 / 5) * celsius + 32
"""

# Enter Celsius
celsius = eval(input('Enter a degree in Celsius: '))

# convert Celsius to Fahrenheit
fahrenheit = (9 / 5) * celsius + 32

# display the result
print(f'{celsius} Celsius is {fahrenheit} Fahrenheit')
