"""
2.2 (Compute the volume of a cylinder) Write a program that reads in the radius and
length of a cylinder and computes the area and volume using the following formulas:
    area = radius * radius * π
    volume = area * length
"""

# Enter the radius and length of a cylinder
radius, length = eval(input('Enter the radius and length of a cylinder: '))

# compute the cylinders' area
# I assume pi = 3.1415
area = radius ** 2 * 3.1415

# compute the cylinders' volume
volume = area * length

# display the results
print('The area is ', area)
print('The volume is ', volume)

# note: the difference between the results depends on pi value

