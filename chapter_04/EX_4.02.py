"""
*4.2 (Game: add three numbers) The program in Listing 4.1 generates two integers and
prompts the user to enter the sum of these two integers. Revise the program to generate three single-digit integers and prompt the user to enter the sum of these three
integers.

"""
import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)

answer = eval(input(f'What is {num1} + {num2} + {num3} ? ').strip())

print(f'{num1} + {num2} + {num3} = {answer} is {num1 + num2 + num3 == answer}')
