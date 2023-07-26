"""
1.15 (Turtle: draw two triangles) Write a program that draws two triangles as shown in
Figure 1.18d
"""

import turtle

t = turtle.Turtle()


t.right(60)
t.forward(100)

t.right(-60)
t.back(100)

t.left(60)
t.forward(200)

t.left(-60)
t.back(100)

t.right(60)
t.forward(100)

turtle.done()

