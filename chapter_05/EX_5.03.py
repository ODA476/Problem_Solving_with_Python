"""
5.3 (Conversion from kilograms to pounds) Write a program that displays the following table (note that 1 kilogram is 2.2 pounds):
"""
print('Kilograms     Pounds')
for i in range(1, 200, 2):
    # (12*' '): for style
    print(i, 12*' ', format(i*2.2, '.1f'))
