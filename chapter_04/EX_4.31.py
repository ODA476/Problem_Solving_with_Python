"""
*4.31 (Geometry: point position) Given a directed line from point p0(x0, y0) to p1(x1,
y1), you can use the following condition to decide whether a point p2(x2, y2) is
on the left side of the line, on the right side of the line, or on the same line (see
Figure 4.12):
(x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)
>0 p2 is on the left side of the line
=0 p2 is on the same line
<0 p2 is on the right side of the line

Write a program that prompts the user to enter the x- and y-coordinates for the
three points p0, p1, and p2 and displays whether p2 is on the left side of the line
from p0 to p1, on the right side, or on the same line.
"""

# Enter coordinates for the three points p0, p1, and p2
x0, y0, x1, y1, x2, y2 = eval(input('Enter coordinates for the three points p0, p1, and p2: ').strip())

# look at description of the question to know how we compute the condition
condition = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

if condition > 0:  # the point is on the left side of the line
    print('p2 is on the left side of the line from p0 to p1')
elif condition < 0:  # the point is on the right side of the line
    print('p2 is on the right side of the line from p0 to p1')
else:  # the point is on the same line
    print('p2 is on the same line from p0 to p1')
