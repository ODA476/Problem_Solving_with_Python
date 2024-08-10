"""
*4.33 (Decimal to hex) Write a program that prompts the user to enter an integer
between 0 and 15 and displays its corresponding hex number.
"""

# Enter a decimal value
value = eval(input('Enter a decimal value (0 to 15): ').strip())

# check if value between 0 and 15
if 0 <= value <= 15:
    # the hex() function convert any decimal number to hexadecimal number
    print(hex(value)[2])
else:
    print('Invalid input')
