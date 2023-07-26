"""
2.4 (Convert pounds into kilograms) Write a program that converts pounds into
kilograms. The program prompts the user to enter a value in pounds, converts it to
kilograms, and displays the result. One pound is 0.454 kilograms.
    kilogram = pound * 0.454
"""

# Enter the value in pound
pound = eval(input('Enter a value in pounds: '))

# convert pound to kilograms
kilogram = pound * 0.454

# display the result
print(f'{pound} pounds is {kilogram} kilograms')


