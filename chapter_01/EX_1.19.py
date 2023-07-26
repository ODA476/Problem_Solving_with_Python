"""
1.19 (Turtle: draw a polygon) Write a program that draws a polygon that connects the
points (40, -69.28), (-40, -69.28), (-80, -9.8), (-40, 69), (40, 69), and (80,
0) in this order, as shown in Figure 1.20a.
"""

import turtle as t

t.penup()
t.goto(40, -69.28)
t.pendown()
t.goto(-40, -69.28)
t.goto(-80, -9.8)
t.goto(-40, 69)
t.goto(40, 69)
t.goto(80, 0)
# to close the loop
t.goto(40, -69.28)

t.done()
