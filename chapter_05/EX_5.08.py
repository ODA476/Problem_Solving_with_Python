import math

# for pattern
print('Number\t\tSquare Root')

# display from 0 to 20.
for num in range(0, 21, 2):
    print(f'{num}\t\t\t{format(math.sqrt(num), ".4f")}')


