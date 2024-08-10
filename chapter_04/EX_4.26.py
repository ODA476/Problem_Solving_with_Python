"""
4.26 (Palindrome number) Write a program that prompts the user to enter a three-digit
integer and determines whether it is a palindrome number. A number is a palindrome
if it reads the same from right to left and from left to right
"""
import sys

# Enter a three-digit integers
num = int(input('Enter a three-digit integer: ').strip())

# check if number have more 3 digits
if num > 999:
    print('The integer number that it is Entered have more 3 digit.')
    sys.exit()

# The three digits integer is palindrome, if first digit equals last digit.

# compute first digit
first_digit = num // 100

# compute last digit
last_digit = num % 10

if first_digit == last_digit:
    print(f'{num} is a palindrome.')

else:
    print(f'{num} is not a palindrome.')
