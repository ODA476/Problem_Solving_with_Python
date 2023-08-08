"""
4.7 (Financial application: monetary units) Modify Listing 3.4, ComputeChange.py,
to display the nonzero denominations only, using singular words for single units
such as 1 dollar and 1 penny, and plural words for more than one unit such as 2
dollars and 3 pennies.
"""

# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display the results
print('Your amount', amount, 'consists of')
if numberOfOneDollars != 0:
    print("\t", numberOfOneDollars, "dollars")

if numberOfQuarters != 0:
    print("\t", numberOfQuarters, "quarters")

if numberOfDimes != 0:
    print("\t", numberOfDimes, "dimes")

if numberOfNickels != 0:
    print("\t", numberOfNickels, "nickels")

if numberOfPennies != 0:
    print("\t", numberOfPennies, "pennies")
