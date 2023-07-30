"""
*2.20 (Financial application: calculate interest) If you know the balance and the annual
percentage interest rate, you can compute the interest on the next monthly payment using the following formula:
    interest = balance * (annualInterestRate / 1200)
Write a program that reads the balance and the annual percentage interest rate
and displays the interest for the next month.
"""

# Enter balance and interest rate (e.g., 3 for 3%)
balance, annual_interest_rate = eval(input('Enter balance and interest rate (e.g., 3 for 3%): '))

# calculate interest
interest = balance * (annual_interest_rate / 1200)

# display interest
print(f'The interest is {interest:.5f}')
