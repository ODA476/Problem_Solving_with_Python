"""
3.4 (Geometry: area of a pentagon) The area of a pentagon can be computed using the
following formula (s is the length of a side):
    area = (5 * s ** 2) / (4 * tan(pi / 5))
Write a program that prompts the user to enter the side of a pentagon and displays
the area.
"""
import math

# Enter the side
side = eval(input('Enter the side: ').strip())

# compute area of pentagon
area = (5 * side ** 2) / (4 * math.tan(math.pi / 5))

# display the rseult
print('The area of the pentagon is', area)
