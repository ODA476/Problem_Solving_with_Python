"""
2.16 (Physics: acceleration) Average acceleration is defined as the change of velocity
divided by the time taken to make the change, as shown in the following formula:
    a = (v1 - v0) / t
Write a program that prompts the user to enter the starting velocity v0 in
meters/second, the ending velocity in meters/second, and the time span t in
seconds, and displays the average acceleration.
"""

# Enter v0, v1, and t
v0, v1, t = eval(input('Enter v0, v1, and t: '))

# compute the average acceleration
a = (v1 - v0) / t

# display the result
print(f'The average acceleration is {a:.4f}')

