"""
*3.5 (Geometry: area of a regular polygon) A regular polygon is an n-sided polygon in
which all sides are of the same length and all angles have the same degree (i.e., the
polygon is both equilateral and equiangular). The formula for computing the area
of a regular polygon is
    area = (n * s ** 2) / (4 * tan(pi / 5))
Here, s is the length of a side. Write a program that prompts the user to enter the
number of sides and their length of a regular polygon and displays its area.
"""

import math

# Enter the number of sides
n = eval(input('Enter the number of sides: ').strip())

# Enter the side
side = eval(input('Enter the side: ').strip())

# compute area of pentagon
area = (n * side ** 2) / (4 * math.tan(math.pi / 5))

# display the rseult
print('The area of the polygon is', area)
