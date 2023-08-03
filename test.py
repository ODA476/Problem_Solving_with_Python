import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

answer = eval(input(f'What is {num1} + {num2}? ').strip())

print(f'{num1} + {num2} = {answer} is {answer == num1 + num2}')
