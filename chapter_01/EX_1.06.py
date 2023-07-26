# 1.6 (Summation of a series) Write a program that displays the result of
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9

# first solution (base solution for chapter #1)
print('1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = ', end='')
print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)

# second solution >> it depends on (for Loop) Chapter #5
result = 0
for i in range(1, 10):
    result += i

print('1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = ', end='')
print(result)

