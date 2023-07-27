"""
*2.10 (Physics: find runway length) Given an airplane’s acceleration a and take-off
speed v, you can compute the minimum runway length needed for an airplane to
take off using the following formula:
    length = v ** 2 / (2 * a)
Write a program that prompts the user to enter v in meters/second (m/s) and the
acceleration a in meters/second squared and displays the minimum runway
length.
"""

# Enter speed and acceleration
v, a = eval(input('Enter speed and acceleration: '))

# compute the minimum runway length
length = v ** 2 / (2 * a)

# display the result
print(f'The minimum runway length for this airplane is {length:.3f} meters')
