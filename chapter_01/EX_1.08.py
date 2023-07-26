"""
1.8 (Area and perimeter of a circle) Write a program that displays the area and
perimeter of a circle that has a radius of 5.5 using the following formulas:
perimeter = 2 * radius * pi
area = radius * radius * pi
"""
import math
# pi = 3.141592653589793, this provides from math class from standard python. You can replace pi by 3.14
# format f allow to write a variable in '' (string)
"""
In addition,
if you want to display only 3, more, or less digit after point.
You can use this format {float_number:.nf}.
n: number of digit
for example, (34.55751918948772):.3f = 34.558
"""
# calculate area

# first solution
print('area = 5.5 * 5.5 * pi = ', end='')
print(pow(5.5, 2) * math.pi)

# second solution
print(f'area = 5.5 * 5.5 * pi = {pow(5.5, 2) * math.pi}')

# calculate perimeter

# first solution
print('perimeter = 2 * 5.5 * pi = ', end='')
print(2 * 5.5 * math.pi)

# second solution
print(f'perimeter = 2 * 5.5 * pi = {2 * 5.5 * math.pi}')
