"""
**4.4 (Game: learn addition) Write a program that generates two integers under 100 and
prompts the user to enter the sum of these two integers. The program then reports
true if the answer is correct, false otherwise. The program is similar to Listing 4.1.
"""

import random

# generate two number between 0 and 100
num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

# Enter answer of num1 + num2
answer = eval(input(f'What is {num1} + {num2} ? ').strip())

# display the result
print(f'{num1} + {num2} = {answer} is {num1 + num2 == answer}')
