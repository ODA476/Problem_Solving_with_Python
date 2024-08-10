# counts of times
times = 0

# this values at initially
miles = 1
kilometers = 20


print('Miles\t\tKilometers\t|\tKilometers\t\tMiles')
while times != 10:
    print(f'{miles}\t\t\t{format(miles * 1.609, ".3f")} \t\t|\t{kilometers}\t\t\t\t{format((kilometers / 1.609), ".3f")}')

    times += 1
    miles += 1
    kilometers += 5


