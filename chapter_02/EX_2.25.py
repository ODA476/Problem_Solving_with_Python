"""
**2.25 (Turtle: draw a rectangle) Write a program that prompts the user to enter the
center of a rectangle, width, and height, and displays the rectangle, as shown in
Figure 2.4c
"""
import math
import turtle as t

# Enter the center of a rectangle
x, y = eval(input('Enter the center of a rectangle: '))

# Enter width, and height
width, height = eval(input('Enter the width and the height (NOTE: the width < the height): '))

# calculate the square diameter
diameter = (width ** 2 + height ** 2) ** 0.5
print(diameter)

# calculate the angle value

# Calculate the angle in radians
angle_radians = math.asin(height / diameter)

# Convert radians to degrees
angle_degrees = math.degrees(angle_radians)

print(angle_degrees)

# draw the rectangle

# to go to beginning point to draw
t.penup()
t.goto(x, y)
t.left(90 + (90 - angle_degrees))
t.forward(diameter / 2)

# start draw rectangle
#
t.right(90 + (90 - angle_degrees))
t.pendown()
t.forward(width)

t.right(90)
t.forward(height)

t.right(90)
t.forward(width)

t.right(90)
t.forward(height)

t.done()
