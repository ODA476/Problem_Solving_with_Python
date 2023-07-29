"""
*2.13 (Split digits) Write a program that prompts the user to enter a four-digit integer
and displays the number in reverse order.
"""

# Enter an integer number
number = int(input('Enter an integer: '))

thousands = number // 1000 % 10
print(thousands)
hundreds = number // 100 % 10
print(hundreds)
twos = number // 10 % 10
print(twos)
ones = number // 1 % 10
print(ones)

# second solution for loop
# for i in str(number):
#     print(i)



