"""
**4.19 (Compute the perimeter of a triangle) Write a program that reads three edges for a
triangle and computes the perimeter if the input is valid. Otherwise, display that
the input is invalid. The input is valid if the sum of every pair of two edges is
greater than the remaining edge.
"""

# Enter three edges
e1, e2, e3 = eval(input('Enter three edges: ').strip())

# check if input is valid or invalid
if (e1 + e2 > e3) and (e1 + e3 > e2) and (e2 + e3 > e1):
    # e1 + e2 + e3 >> compute the perimeter.
    print(f'The perimeter is {e1 + e2 + e3}.')
else:
    print('The input is invalid.')
