"""
1.17 (Turtle: draw a line) Write a program that draws a red line connecting two points
(-39, 48) and (50, -50) and displays the coordinates of the two points, as shown
in Figure 1.19b.
"""

import turtle as t

t.penup()
t.goto(-39, 48)
t.write('(-39, 48)')
t.pendown()
t.goto(50, -50)
t.write('(50, -50)')

# to hide the pen pointer
t.color('white')

t.done()
