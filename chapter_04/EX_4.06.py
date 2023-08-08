"""
*4.6 (Health application: BMI) Revise Listing 4.6, ComputeBMI.py, to let users enter
their weight in pounds and their height in feet and inches. For example, if a person
is 5 feet and 10 inches, you will enter 5 for feet and 10 for inches
"""

# Listing 4.6 >> ComputeBMI.py with some editions

# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: ").strip())

# Prompt the user to enter feet
feet = eval(input("Enter feet: ").strip())

# Prompt the user to enter feet
inches = eval(input("Enter inches: ").strip())

KILOGRAMS_PER_POUND = 0.45359237  # Constant
METERS_PER_INCH = 0.0254  # Constant
METERS_PER_FEET = 0.3048  # Constant

# Compute BMI
weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = (inches * METERS_PER_INCH) + (feet * METERS_PER_FEET)
bmi = weightInKilograms / (heightInMeters * heightInMeters)

# Display result
print("BMI is", bmi)
if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You are Normal")
elif bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")
