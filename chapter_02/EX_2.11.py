"""
*2.11 (Financial application: investment amount) Suppose you want to deposit a
certain amount of money into a savings account with a fixed annual interest rate.
What amount do you need to deposit in order to have $5,000 in the account after
three years? The initial deposit amount can be obtained using the following
formula:
        initialDepositAmount = finalAccountValue / (1 + monthlyInterestRate) **  numberOfMonths
Write a program that prompts the user to enter final account value, annual interest
rate in percent, and the number of years, and displays the initial deposit amount.
"""

# Enter final account value
final_account_value = eval(input('Enter final account value: '))

# Enter annual interest rate in percent (/100)
annual_interest_rate = eval(input('Enter annual interest rate in percent: ')) / 100

# calculate monthly interest rate, by divide 12
monthly_interest_rate = annual_interest_rate / 12

# Enter number of years
number_of_years = eval(input('Enter number of year: '))

# compute number of month
number_of_months = number_of_years * 12

# compute initial deposit value
initial_deposit_value = final_account_value / ((1 + monthly_interest_rate) ** number_of_months)

# display the result
print('Initial deposit value is ', initial_deposit_value)




