import random
import time

correctCount = 0
count = 0
NUMBER_OF_QUESTIONS = 10

startTime = time.time() # Get start time

while count < NUMBER_OF_QUESTIONS:
    # Generate two random single-digit integers
    number1 = random.randint(1, 15)
    number2 = random.randint(1, 15)

    # Prompt the student to answer "What is number1 - number2?"
    answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))
    # Grade the answer and display the result
    if number1 + number2 == answer:
        print("You are correct!")
    else:
        print("Your answer is wrong.\n", number1, "+", number2, "is", number1 - number2)
    # Increase the count

    endTime = time.time()  # Get end time
    testTime = int(endTime - startTime)  # Get test time
    print("Correct count is", correctCount, "out of", NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")
