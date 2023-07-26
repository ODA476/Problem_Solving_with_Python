# 1.7 (Approximate pi) pi can be computed using the following formula

# first solution
print(4 * (1 - (1 / 3) + (1 / 5) - (1 / 7) + (1 / 9) - (1 / 11)))
print(4 * (1 - (1 / 3) + (1 / 5) - (1 / 7) + (1 / 9) - (1 / 11) + (1 / 13) - (1 / 15)))

# second solution
result = 0
num_of_algebraic_limit = 7
for i, j in zip(range(1, num_of_algebraic_limit), range(1, 12, 2)):
    if i % 2 == 0:
        result += (-1 / j)
    else:
        result += (1 / j)

print(4 * result)


# third solution
result = 0
for i in range(1, 7):
    result += (1/(pow(-1, i+1) * (2*i - 1)))

print(4 * result)
