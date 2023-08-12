"""
*4.25 (Geometry: intersecting point) Two points on line 1 are given as (x1, y1) and (x2,
y2) and on line 2 as (x3, y3) and (x4, y4), as shown in Figure 4.9a–b.

The intersecting point of the two lines can be found by solving the following linear equation:
(y1 - y2)x - (x 1 - x 2)y = (y1 - y2)x 1 - (x 1 - x 2)y1
(y3 - y4)x - (x 3 - x 4)y = (y3 - y4)x 3 - (x 3 - x 4)y3

This linear equation can be solved using Cramer’s rule (see Exercise 4.3). If the
equation has no solutions, the two lines are parallel (Figure 4.9c). Write a program
that prompts the user to enter four points and displays the intersecting point.

# NOTE: from EX_4.3 >>
You can use Cramer’s rule to solve the
following system of linear equation:
    ax + by = e
    cx + dy = f
    x = (ed - bf) / (ad - bc)
    y = (af - ec) / (ad - bc)
(If ad – bc is 0, report that The equation has no solution.)

a = y1 - y2
b = x2 - x1
e = (y1 - y2) * x1 - (x1 - x2) * y1

c = y3 - y4
d = x4 - x3
f = (y3 - y4) * x3 - (x3 - x4) * y3
"""

# Enter x1, y1, x2, y2, x3, y3, x4, y4
x1, y1, x2, y2, x3, y3, x4, y4 = eval(input('Enter x1, y1, x2, y2, x3, y3, x4, y4: ').strip())

# compute a, b, c, d, e, f
a = y1 - y2
b = x2 - x1
e = (y1 - y2) * x1 - (x1 - x2) * y1
c = y3 - y4
d = x4 - x3
f = (y3 - y4) * x3 - (x3 - x4) * y3

if (a * d) == (b * c):
    # if ad - bc = 0 >> the equation has no solution
    print('The two lines are parallel')
else:
    # ab - bc  not equal 0 >> the equation has solution
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print(f'The intersecting point is at ({x:.4f}, {y:.4f})')
