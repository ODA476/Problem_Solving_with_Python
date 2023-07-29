"""
2.12 (Print a table) Write a program that displays the following table:
a   b   a ** b
1   2   1
2   3   8
3   4   81
4   5   1024
5   6   15625
"""

# first solution without loop
print('a        b       a ** b')
print(f'1        2       {1 ** 2}')
print(f'2        3       {2 ** 3}')
print(f'3        4       {3 ** 4}')
print(f'4        5       {4 ** 5}')
print(f'5        6       {5 ** 6}')

# second solution by for loop
# print('a        b       a ** b')
# for i in range(1, 6):
#     print(f'{i}        {i+1}       {i ** (i+1)}')
