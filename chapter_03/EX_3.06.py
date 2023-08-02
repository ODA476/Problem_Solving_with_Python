"""
*3.6 (Find the character of an ASCII code) Write a program that receives an ASCII
code (an integer between 0 and 127) and displays its character. For example, if the
user enters 97, the program displays the character a.

NOTE 0: if user Entered number > 127. He has a runtime error.
to avoid this error. read NOTE 1 , and NOTE 2

NOTE 1: This Exercise must be at chapter 4, because it needs if statement.
here at chapter 3. The beginner student doesn't learn the selections.

NOTE 2: The answer for this question will be depending on if statement (chapter 4)
"""

# Enter an ASCII code
ascii_code = int(input('Enter an ASCII code: ').strip())

if 0 < ascii_code < 127:
    print(f'The character is {chr(ascii_code)}')
else:
    print(f'There is no {ascii_code} Code')




