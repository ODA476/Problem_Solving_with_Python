"""
2.24 (Turtle: draw four hexagons) Write a program that draws four hexagons in the
center of the screen, as shown in Figure 2.4b.
"""
import turtle as t

# Enter the center
x, y = eval(input('Enter the center (x, y): '))

t.speed(2)
t.penup()
t.goto(x, y)

t.goto(x + 40, y)
t.pendown()
t.circle(40, steps=6)

t.penup()
t.goto(x - 40, y)
t.pendown()
t.circle(40, steps=6)

t.penup()
t.goto(x - 40, y - 80)
t.pendown()
t.circle(40, steps=6)

t.penup()
t.goto(x + 40, y - 80)
t.pendown()
t.circle(40, steps=6)

t.hideturtle()

t.done()
