"""
3.1 (Geometry: area of a pentagon) Write a program that prompts the user to enter the
length from the center of a pentagon to a vertex and computes the area of the pentagon
The formula for computing the area of a pentagon is
    area = 3 * sqrt(3) * s ** 2 / 2,
where s is the length of a side.
The side can be computed using the formula
    s = 2 * r * sin(pi/5)
where r is the length from the center of a pentagon to a vertex
"""
import math

# Enter the length from the center to a vertex
length = eval(input('Enter the length from the center to a vertex: '))

# compute s from previous formula
s = 2 * length * math.sin(math.pi / 5)

# calculate the area
area = 3 * math.sqrt(3) * s ** 2 / 2

# display the area
print('The area of the pentagon is ', format(area, '.2f'))
