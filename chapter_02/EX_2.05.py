"""
*2.5 (Financial application: calculate tips) Write a program that reads the subtotal and
the gratuity rate and computes the gratuity and total. For example, if the user
enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
as the gratuity and 11.5 as the total.
"""

# Enter the subtotal and a gratuity rate
subtotal, gratuity_rate = eval(input('Enter the subtotal and a gratuity rate: '))

# compute the gratuity,
# gratuity = subtotal * gratuity_rate
# I divided by 100, because I want gratuity_rate as percentage
gratuity = subtotal * (gratuity_rate / 100)

# compute the total.
# total = subtotal + gratuity
total = subtotal + gratuity

# display the result
# :.2f >> to display only two digit after the point.
print(f'The gratuity is {gratuity:.2f} and the total is {total:.2f}')
