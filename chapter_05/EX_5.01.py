"""
(Count positive and negative numbers and compute the average of numbers)
Write a program that reads an unspecified number of integers, determines
how many positive and negative values have been read, and computes the total
and average of the input values (not counting zeros). Your program ends with the
input 0. Display the average as a floating-point number.
"""
import sys

count_of_positive_numbers = 0
count_of_negative_numbers = 0
count_of_all_inputs = 0
sum_of_numbers = 0

while True:
    # Enter an integer
    value = eval(input('Enter an integer, the input ends if it is 0: ').strip())

    # check the value if it equals zero to exit
    if value == 0:
        print("You didn't enter any number")
        sys.exit()
    else:
        # check type of value (positive or negative)
        if value > 0:
            count_of_positive_numbers += 1
        else:
            count_of_negative_numbers += 1
        # sum the new value to sum
        sum_of_numbers += value

        # update the count of all inputs
        count_of_all_inputs += 1

# compute the average
average = sum_of_numbers / count_of_all_inputs

# print the results
print(f'The number of positives is {count_of_positive_numbers}')
print(f'The number of negatives is {count_of_negative_numbers}')
print(f'The total is {sum_of_numbers}')
print(f'The average is {average}')
