"""
**2.26 (Turtle: draw a circle) Write a program that prompts the user to enter the
center and radius of a circle, and then displays the circle and its area, as shown
in Figure 2.5.
"""
import math
import turtle as t

# Enter the center of circle
x, y = eval(input('Enter the center of circle: '))

# Enter the radius of circle
radius = eval(input('Enter the radius of circle: '))

# calculate the area
area = radius ** 2 * math.pi

t.penup()
t.goto(x, y)
t.write(f'{area:.2f}')

t.left(180)
t.forward(radius)
t.right(180)
t.left(270)

t.pendown()
t.circle(radius)

t.done()
