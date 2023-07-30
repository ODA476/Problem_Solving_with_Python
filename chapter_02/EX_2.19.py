"""
*2.19 (Financial application: calculate future investment value) Write a program that
reads in an investment amount, the annual interest rate, and the number of years,
and displays the future investment value using the following formula:
    futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths
For example, if you enter the amount 1000, an annual interest rate of 4.25%,
and the number of years as 1, the future investment value is 1043.33
"""

# Enter investment amount
investment_amount = eval(input('Enter investment amount: '))

# Enter annual interest rate,
# and convert it to monthly interest rate by divided it by 12
monthly_interest_rate = eval(input('Enter annual interest rate: ')) / 100 / 12

# Enter number of years,
# and convert it to month
number_of_months = eval(input('Enter number of years: ')) * 12

# calculate future investment value
future_investment_value = investment_amount * (1 + monthly_interest_rate) ** number_of_months

# display the result
print(f'Accumulated value is {future_investment_value:.3f}')
