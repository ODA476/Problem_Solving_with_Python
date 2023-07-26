"""
1.12 (Turtle: draw four squares) Write a program that draws four squares in the center
of the screen, as shown in Figure 1.18a.
"""
import turtle

t = turtle.Turtle()

# draw square
for i in range(4):
    t.forward(100)
    t.left(90)

# draw horizontal diameter
t.penup()
t.goto(0, 50)
t.pendown()
t.forward(100)

# draw vertical diameter
t.penup()
t.goto(50, 0)
t.pendown()
t.left(90)
t.forward(100)

turtle.done()
