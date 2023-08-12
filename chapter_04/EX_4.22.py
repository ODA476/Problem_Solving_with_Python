"""
**4.22 (Geometry: point in a circle?) Write a program that prompts the user to enter a
point (x, y) and checks whether the point is within the circle centered at (0, 0) with
radius 10. For example, (4, 5) is inside the circle and (9, 9) is outside the circle, as
shown in Figure 4.8a.

(Hint: A point is in the circle if its distance to (0, 0) is less than or equal to 10. The
formula for computing the distance is sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
"""
import math

# Enter a point with two coordinates
x, y = eval(input('Enter a point with two coordinates: ').strip())

# compute the distance between (0, 0) and (x, y)
# because x2, and x2 equal 0. There is no subtract operation here.
distance = math.sqrt(x ** 2 + y ** 2)

if distance > 10:
    # display result
    print(f'Point ({x}, {y}) is not in the circle.')
else:
    # display result
    print(f'Point ({x}, {y}) is in the circle.')
