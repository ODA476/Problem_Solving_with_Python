"""
*4.9 (Financial: compare costs) Suppose you shop for rice and find it in two differentsized packages. You would like to write a program to compare the costs of the
packages. The program prompts the user to enter the weight and price of each
package and then displays the one with the better price.
"""

# Enter weight and price for package 1
weight1, price1 = eval(input('Enter weight and price for package 1: ').strip())

# Enter weight and price for package 2
weight2, price2 = eval(input('Enter weight and price for package 2: ').strip())

# compute one unit of weight per its price
weight_per_price_1 = weight1 / price1
weight_per_price_2 = weight2 / price2

# choose the better, the better has less cost than other
if weight_per_price_1 < weight_per_price_2:
    print('Package 1 has the better price.')

elif weight_per_price_1 > weight_per_price_2:
    print('Package 2 has the better price.')

else:
    print('Two packages have the same price.')
