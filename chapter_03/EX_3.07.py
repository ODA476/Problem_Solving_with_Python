"""
3.7 (Random character) Write a program that displays a random uppercase letter
using the time.time() function.
"""

import random

# random.randint(a, b):
#   Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

# 65 >> A, 90 >> Z
print(chr(random.randint(65, 90)))
