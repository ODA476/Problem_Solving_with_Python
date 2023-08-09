"""
**4.15 (Game: lottery) Revise Listing 4.10, Lottery.py, to generate a three-digit lottery
number. The program prompts the user to enter a three-digit number and determines whether the user wins according to the following rules:
1. If the user input matches the lottery number in the exact order, the award is
$10,000.
2. If all the digits in the user input match all the digits in the lottery number, the
award is $3,000.
3. If one digit in the user input matches a digit in the lottery number, the award is
$1,000.
"""

import random

# Generate a lottery number
lottery = random.randint(100, 999)
print(lottery)

# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (three digits): "))

# Get digits from lottery
lotteryDigit1 = lottery // 100
lotteryDigit2 = lottery // 10 % 10
lotteryDigit3 = lottery % 10

# Get digits from guess
guessDigit1 = guess // 100
guessDigit2 = guess // 10 % 10
guessDigit3 = guess % 10

print("The lottery number is", lottery)

# Check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif (lotteryDigit1 == guessDigit2 or lotteryDigit1 == guessDigit3) and \
        (lotteryDigit2 == guessDigit1 or lotteryDigit2 == guessDigit3) and \
        (lotteryDigit3 == guessDigit1 or lotteryDigit3 == guessDigit2):
    print("Match all digits: you win $3,000")
elif lotteryDigit1 == guessDigit1 or lotteryDigit1 == guessDigit2 or lotteryDigit1 == guessDigit3 \
        or lotteryDigit2 == guessDigit1 or lotteryDigit2 == guessDigit2 or lotteryDigit2 == guessDigit3 \
        or lotteryDigit3 == guessDigit1 or lotteryDigit3 == guessDigit2 or lotteryDigit3 == guessDigit3:
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
