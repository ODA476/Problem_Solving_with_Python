"""
**2.6 (Sum the digits in an integer) Write a program that reads an integer between 0 and
1000 and adds all the digits in the integer. For example, if an integer is 932, the
sum of all its digits is 14. (Hint: Use the % operator to extract digits, and use the //
operator to remove the extracted digit. For instance, 932 % 10 = 2 and 932 //
10 = 93.)
"""

# Enter a number between 0 and 1000.
# note: 0 < number < 1000, I mean 1000 I can't use it.
number = eval(input('Enter a number between 0 and 1000: '))
"""
In this solution, I will solve this question without check number was entered,
because I assume that the new student hasn't learned if statement.
"""

# to get ones, you must calculate divide 1 and modula 10
ones = number // 1 % 10

# to get tens, you must calculate divide 10 and modula 10
tens = number // 10 % 10

# to get hundreds, you must calculate divide 100 modula 10
hundreds = number // 100 % 10

sum_of_digits = ones + tens + hundreds
print('The sum of the digits is ', sum_of_digits)
