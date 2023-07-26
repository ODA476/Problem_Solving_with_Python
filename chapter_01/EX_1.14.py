"""
1.14 (Turtle: draw a triangle) Write a program that draws a triangle as shown in
Figure 1.18c.
"""

import turtle

t = turtle.Turtle()


t.right(60)
t.forward(100)

t.right(-60)
t.back(100)

t.left(60)
t.forward(100)

turtle.done()

