"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# Answers

# Question 1
# A ValueError occurs when the user enters an input of a specific data type that is not expected by the program.
# In this case, any value that cannot be converted into an integer will return ValueError (e.g. string, float, etc.)

# Question 2
# A ZeroDivisionError will occur when the user enters a Zero (0) for the denominator value.
# Any number divided by 0 is undefined.

# Question 3
# Yes, I can change it by using 'while' error-checking pattern.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Denominator cannot be 0.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")