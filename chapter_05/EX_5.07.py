import math

# for pattern
print('Degree\t\tSin\t\t\tCos')

# display from 0 to 360.
for degree in range(0, 361, 10):
    print(f'{degree}\t\t\t{format(math.sin(math.radians(degree)), ".4f")}\t\t{format(math.cos(math.radians(degree)), ".4f")}')

