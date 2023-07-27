"""
2.8 (Science: calculate energy) Write a program that calculates the energy needed to
heat water from an initial temperature to a final temperature. Your program should
prompt the user to enter the amount of water in kilograms and the initial and final
temperatures of the water. The formula to compute the energy is
    Q = M * (finalTemperature – initialTemperature) * 4184
where M is the weight of water in kilograms, temperatures are in degrees Celsius,
and energy Q is measured in joules.
"""

# Enter the amount of water in kilograms
amount_of_water = eval(input('Enter the amount of water in kilograms: '))

# Enter the initial temperature
initial_temperature = eval(input('Enter the initial temperature: '))

# Enter the final temperature
final_temperature = eval(input('Enter the final temperature: '))

# compute the energy
energy = amount_of_water * (final_temperature - initial_temperature) * 4184

# display the result.
print('The energy needed is ', energy)
