"""
**2.21 (Financial application: compound value) Suppose you save $100 each month into
a savings account with an annual interest rate of 5%. Therefore, the monthly interest rate is After the first month,
the value in the account becomes
    100 * (1 + 0.00417) = 100.417
> After the second month, the value in the account becomes
    (100 + 100.417) * (1 + 0.00417) = 201.252
> After the third month, the value in the account becomes
    (100 + 201.252) * (1 + 0.00417) = 302.507
and so on.

Write a program that prompts the user to enter a monthly saving amount and
displays the account value after the sixth month.
"""

# Enter the monthly saving amount
monthly_saving_amount = eval(input('Enter the monthly saving amount: '))

# first solution without loop
# compute the account value after the first month
account_value = monthly_saving_amount * (1 + 0.00417)

# compute the account value after the second month
account_value = (account_value + monthly_saving_amount) * (1 + 0.00417)

# compute the account value after the third month
account_value = (account_value + monthly_saving_amount) * (1 + 0.00417)

# compute the account value after the fourth month
account_value = (account_value + monthly_saving_amount) * (1 + 0.00417)

# compute the account value after the fifth month
account_value = (account_value + monthly_saving_amount) * (1 + 0.00417)

# compute the account value after the sixth month
account_value = (account_value + monthly_saving_amount) * (1 + 0.00417)

# display the account value, after the sixth month
print(f'After the sixth month, the account value is {account_value:.3f}')


# second solution with loop
# account_value = 0
# for i in range(6):
#     account_value = (account_value + monthly_saving_amount) * (1 + 0.00417)
#
# print(f'After the sixth month, the account value is {account_value:.3f}')