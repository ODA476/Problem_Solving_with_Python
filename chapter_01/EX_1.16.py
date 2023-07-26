"""
1.16 (Turtle: draw four circles) Write a program that draws four circles in the center of
the screen, as shown in Figure 1.19a
"""

import turtle

t = turtle.Turtle()

t.circle(50)

t.penup()
t.forward(100)
t.pendown()
t.circle(50)

t.penup()
t.right(90)
t.forward(100)
t.right(-90)
t.pendown()
t.circle(50)

t.penup()
t.right(180)
t.forward(100)
t.right(-180)
t.pendown()
t.circle(50)

turtle.done()
