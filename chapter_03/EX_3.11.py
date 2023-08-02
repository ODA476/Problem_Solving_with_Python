"""
3.11 (Reverse number) Write a program that prompts the user to enter a four-digit integer
 and displays the number in reverse order.

Note: I think this equation need for loop if it has length > 4
"""

# Enter number
number = input('Enter an integer: ').strip()
# display the result
print(f'The reversed number is {number[3]}{number[2]}{number[1]}{number[0]}')
