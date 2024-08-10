"""
*4.8 (Sort three integers) Write a program that prompts the user to enter three integers
and displays them in increasing order.
"""

# Enter three integers
num1, num2, num3 = eval(input('Enter three integers: ').strip())

# initial, we assume that num1 is max
max = num1

# we will compare about max, if any number is greate than max, we will replace
# select the maximum number
if num2 > max:
    max = num2

if num3 > max:
    max = num3

    # select other order number
if max == num1:
    if num2 > num3:
        print(num3, num2, max)
    else:
        print(num2, num3, max)

elif max == num2:
    if num3 > num1:
        print(num1, num3, max)
    else:
        print(num3, num1, max)
else:
    if num2 > num1:
        print(num1, num2, max)
    else:
        print(num2, num1, max)
