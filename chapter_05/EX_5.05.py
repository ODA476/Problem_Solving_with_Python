# counts of times
times = 0

# this values at initially
kilograms = 1
pounds = 20

# pound = kilogram * 2.2
# kilogram = pound /  2.2
print('Kilograms\t\tPounds\t|\tPounds\t\tKilograms')
while times != 100:
    print(f'{kilograms}\t\t\t\t{format(kilograms * 2.2, ".1f")} \t|\t{pounds}\t\t\t{format((pounds / 2.2), ".2f")}')

    times += 1
    kilograms += 2
    pounds += 5


