"""
*4.1 (Algebra: solve quadratic equations) The two roots of a quadratic equation, for
example, can be obtained using the following formula:
    r1 = (-b + sqrt(b ** 2 - 4 * a * c)) / 2 * a
    r2 = (-b - sqrt(b ** 2 - 4 * a * c)) / 2 * a
(b ** 2 - 2 * a * c) is called the discriminant of the quadratic equation. If it is positive, the
equation has two real roots. If it is zero, the equation has one root. If it is negative,
the equation has no real roots.

Write a program that prompts the user to enter values for a, b, and c and displays
the result based on the discriminant. If the discriminant is positive, display two
roots. If the discriminant is 0, display one root. Otherwise, display The equation has no real roots.
"""
import math

# Enter a, b, c
a, b, c = eval(input('Enter a, b, c: ').strip())

# calculate the discriminant of the quadratic equation
discriminant_of_the_quadratic_equation = b ** 2 - 4 * a * c

# check
if discriminant_of_the_quadratic_equation == 0:
    # we have one root
    r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    # display the root
    print('The root is', format(r1, ".3f"))
elif discriminant_of_the_quadratic_equation > 0:
    # we have two roots
    r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    # display the result
    print(f'The roots are {r1:.3f} and {r2:.3f}')
else:
    # there is no real roots
    print('The equation has no real roots')
