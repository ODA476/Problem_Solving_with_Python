"""
*4.17 (Game: scissor, rock, paper) Write a program that plays the popular scissor-rockpaper game.
(A scissor can cut a paper, a rock can knock a scissor, and a paper can
wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
2 and displays a message indicating whether the user or the computer wins, loses,
or draws.
"""

# Note: All if sentences block are repeated. we can replace it by function at chapter 6

import random
import sys

# generate computer choice
computer_choice = random.randint(0, 2)

# determine the name of computer choice
if computer_choice == 0:
    computer_choice_name = 'scissor'
elif computer_choice == 1:
    computer_choice_name = 'rock'
else:
    computer_choice_name = 'paper'

# Enter your choice
user_choice = int(input('scissor (0), rock (1), paper (2): ').strip())

# determine the name of computer choice
if user_choice == 0:
    user_choice_name = 'scissor'
elif user_choice == 1:
    user_choice_name = 'rock'
elif user_choice == 2:
    user_choice_name = 'paper'
else:
    print('your choice dose not exists.')
    sys.exit()


if computer_choice == user_choice:
    print(f'The computer is {computer_choice_name}. You are {user_choice_name} too. It is a draw')

elif computer_choice == 0:
    if user_choice == 1:
        print(f'The computer is {computer_choice_name}. You are {user_choice_name}. You Won.')
    else:
        print(f'The computer is {computer_choice_name}. You are {user_choice_name}. You lost.')

elif computer_choice == 1:
    if user_choice == 0:
        print(f'The computer is {computer_choice_name}. You are {user_choice_name}. You lost.')
    else:
        print(f'The computer is {computer_choice_name}. You are {user_choice_name}. You Won.')

else:
    if user_choice == 0:
        print(f'The computer is {computer_choice_name}. You are {user_choice_name}. You Won.')
    else:
        print(f'The computer is {computer_choice_name}. You are {user_choice_name}. You lost.')

