"""
*4.3 (Algebra: solve linear equations) You can use Cramer’s rule to solve the
following system of linear equation:
    ax + by = e
    cx + dy = f
    x = (ed - bf) / (ad - bc)
    y = (af - ec) / (ad - bc)
Write a program that prompts the user to enter a, b, c, d, e, and f and display the
result. If ad – bc is 0, report that The equation has no solution.
"""

# Enter a, b, c, d, e, f
a, b, c, d, e, f = eval(input('Enter a, b, c, d, e, f: ').strip())

if (a * d) == (b * c):
    # if ad - bc = 0 >> the equation has no solution
    print('The equation has no solution')
else:
    # ab - bc  not equal 0 >> the equation has solution
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print(f'x is {x:.1f} and y is {y:.1f}')
