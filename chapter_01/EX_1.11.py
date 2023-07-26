"""
*1.11 (Population projection) The US Census Bureau projects population based on the
following assumptions:
        One birth every 7 seconds
        One death every 13 seconds
        One new immigrant every 45 seconds
Write a program to display the population for each of the next five years. Assume the
current population is 312032486 and one year has 365 days. Hint: in Python, you
can use integer division operator // to perform division. The result is an integer. For
example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
"""
# current population
current_population = 312032486
# step #1, we calculate second in 5 years.
# 24 * 3600 >> number of second in one day.
second_per_years = 24 * 3600 * 365

# step #2, we calculate, How many (7, 13, 45) second
births_per_year = second_per_years // 7
deaths_per_year = second_per_years // 13
immigrants_per_year = second_per_years // 45

# step #3, we calculate the population increasing
# birth +
# death -
# immigrant +
population_increase = births_per_year - deaths_per_year + immigrants_per_year

for i in range(1, 6):
    current_population += population_increase
    print(f'year {i}: {current_population}')
