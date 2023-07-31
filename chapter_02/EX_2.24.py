"""
2.24 (Turtle: draw four hexagons) Write a program that draws four hexagons in the
center of the screen, as shown in Figure 2.4b.
"""
import turtle as t

# Enter the center
x, y = eval(input('Enter the center (x, y): '))

t.penup()
t.goto(x, y)
t.write('0')

t.forward(30)
t.left(120)
t.pendown()
t.forward(50)

t.right(120 - 90)
t.forward(50)

t.right(120 - 90)
t.forward(50)

t.right(120)
t.forward(50)



t.done()
