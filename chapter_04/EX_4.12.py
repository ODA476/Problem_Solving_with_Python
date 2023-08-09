"""
4.12 (Check a number) Write a program that prompts the user to enter an integer and
checks whether the number is divisible by both 5 and 6, divisible by 5 or 6, or just
one of them (but not both)
"""

# Enter an integer
integer_number = int(input('Enter an integer: ').strip())

# check
# Is divisible by both 5 and 6
is_divisible_by_both_5_and_6 = integer_number % 5 == 0 and integer_number % 6 == 0

# Is divisible by both 5 or 6
is_divisible_by_5_or_6 = integer_number % 5 == 0 or integer_number % 6 == 0

# Is divisible by 5 or 6, but not both
is_divisible_by_5_or_6_but_not_both = is_divisible_by_5_or_6 and not is_divisible_by_both_5_and_6

# display result

# Is integer number divisible by 5 and 6?
print(f'Is {integer_number} divisible by 5 and 6? {is_divisible_by_both_5_and_6}')

# Is integer number divisible by 5 or 6?
print(f'Is {integer_number} divisible by 5 or 6? {is_divisible_by_5_or_6}')

# Is integer number divisible by 5 or 6, but not both? True
print(f'Is {integer_number} divisible by 5 or 6, but not both? {is_divisible_by_5_or_6_but_not_both}')
