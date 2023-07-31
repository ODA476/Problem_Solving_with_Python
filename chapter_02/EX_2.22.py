"""
2.22 (Population projection) Rewrite Exercise 1.11 to prompt the user to enter the
number of years and displays the population after that many years.
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

# Enter the number of years (this part spacial with chapter 2)
number_of_years = int(input('Enter the number of years: '))

for i in range(1, number_of_years + 1):
    current_population += population_increase
    print(f'year {i}: {current_population}')
