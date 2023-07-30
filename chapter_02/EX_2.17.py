"""
*2.17 (Health application: compute BMI) Body mass index (BMI) is a measure of health
based on weight. It can be calculated by taking your weight in kilograms and
dividing it by the square of your height in meters. Write a program that prompts
the user to enter a weight in pounds and height in inches and displays the BMI.
Note that one pound is 0.45359237 kilograms and one inch is 0.0254 meters.
"""

# Enter weight in pounds,
# and convert pounds to kilograms.
# weight in kilograms = weight in pounds * 0.45359237
weight = eval(input('Enter weight in pounds: ')) * 0.45359237

# Enter height in inches,
# and convert inches to meters.
# height in meters = height in inches *  0.0254
height = eval(input('Enter height in inches: ')) * 0.0254

# compute BMI
# BMI = weight * (height) ** 2
BMI = weight / height ** 2

# display the result
print(f'BMI is {BMI:.4f}')
