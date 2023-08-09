"""
4.14 (Game: heads or tails) Write a program that lets the user guess whether a flipped
coin displays the head or the tail. The program randomly generates an integer 0 or
1, which represents head or tail. The program prompts the user to enter a guess
and reports whether the guess is correct or incorrect.
"""
import random

# head is 0, and tail is 1
# generate integer numbers 0, or 1
status = random.randint(0, 1)

# Enter your guess only (0, 1)
guess = int(input('Enter your guess (0, 1): ').strip())

print(f'your guess ({"head" if guess == 0 else "tail"}) is {status == guess}')
