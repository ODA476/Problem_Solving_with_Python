"""
**1.18 (Turtle: draw a star) Write a program that draws a star, as shown in Figure 1.19c.
(Hint: The inner angle of each point in the star is 36 degrees.)
"""

import turtle as t

# first solution
t.forward(150)

t.right(180 - 36)
t.forward(150)

t.left(-(180 - 36))
t.forward(150)

t.right(180 - 36)
t.forward(150)

t.left(-(180 - 36))
t.forward(150)


# second solution
# t.penup()
# t.goto(0, 80)
# t.pendown()
# t.goto(60, -80)
# t.goto(-100, 20)
# t.goto(100, 20)
# t.goto(-60, -80)
# t.goto(0, 80)

t.done()
