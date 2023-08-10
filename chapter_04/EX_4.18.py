"""
*4.18 (Financials: currency exchange) Write a program that prompts the user to enter
the currency exchange rate between U.S. dollars and Chinese Renminbi (RMB).
Prompt the user to enter 0 to convert from U.S. dollars to Chinese RMB and 1 for
vice versa. Prompt the user to enter the amount in U.S. dollars or Chinese RMB to
convert it to Chinese RMB or U.S. dollars, respectively.
"""
import sys

# Enter the exchange rate from dollars to RMB
exchange_rate = eval(input('Enter the exchange rate from dollars to RMB: ').strip())

# Enter 0 to convert dollars to RMB and 1 vice versa
status = int(input('Enter 0 to convert dollars to RMB and 1 vice versa: ').strip())

# check the type of exchange
if status == 0: # dollars to yuan

    # Enter the dollar amount
    dollars = eval(input('Enter the dollars amount: ').strip())

    # exchange dollars to yuan
    yuan = dollars * exchange_rate

    # display result
    print(f'${dollars} is {yuan:.2f} yuan')

elif status == 1: # yuan to dollars

    # Enter the yuan amount
    yuan = eval(input('Enter the yuan amount: ').strip())

    # exchange yuan to dollars
    dollars = yuan / exchange_rate

    # display result
    print(f'{yuan} yuan is ${dollars:.2f}')

else:
    print('Incorrect input')
    sys.exit()

