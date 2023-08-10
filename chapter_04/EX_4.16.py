"""
4.16 (Random character) Write a program that displays a random uppercase letter.
"""

import random

# generate ASCII character between 65-90 = A-Z
char = random.randint(65, 90)

# display result
print(chr(char))
