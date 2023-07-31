"""
2.23 (Turtle: draw four circles) Write a program that prompts the user to enter the
radius and draws four circles in the center of the screen, as shown in Figure 2.4a.
"""

import turtle as t

# Enter the radius
radius = eval(input('Enter the radius: '))

t.circle(radius)

t.penup()
t.forward(radius * 2)
t.pendown()
t.circle(radius)

t.penup()
t.right(90)
t.forward(radius * 2)
t.right(-90)
t.pendown()
t.circle(radius)

t.penup()
t.right(180)
t.forward(radius * 2)
t.right(-180)
t.pendown()
t.circle(radius)

t.done()
