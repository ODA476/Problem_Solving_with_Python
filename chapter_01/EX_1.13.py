# 1.13 (Turtle: draw a cross) Write a program that draws a cross as shown in Figure 1.18b

import turtle

t = turtle.Turtle()

# horizontal diameter
t.forward(100)

# move to (50,50) point and direct to down by right 90 degree
t.penup()
t.goto(50, 50)
t.pendown()
t.right(90)

# vertical diameter
t.forward(100)

turtle.done()
