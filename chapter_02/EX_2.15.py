"""
2.15 (Geometry: area of a hexagon) Write a program that prompts the user to enter the
side of a hexagon and displays its area. The formula for computing the area of a
hexagon is Area = (3 * 3**0.5) * s**2 / 2 ,
where s is the length of a side
"""

# Enter the side
side = eval(input('Enter the side: '))

# compute the area
area = ((3 * 3**0.5) / 2) * (side ** 2)

# display the result
print('The area of the hexagon is: {area:.4f}')
