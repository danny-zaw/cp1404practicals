"""
CP1404 - Prac 4
Lists Warmup
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# PART 1

# 1. 3
# 2. 2
# 3. 1
# 4. [3, 1, 4, 1, 5, 9]
# 5. [1]
# 6. True
# 7. False
# 8. False
# 9. [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# PART 2

# 1. Change the first element of numbers to "ten" (the string, not the number 10)

numbers[0] = "ten"

# 2. Change the last element of numbers to 1

numbers[-1] = 1

# 3. Print all the elements from numbers except the first two (slice)

print(numbers[2:])

# 4. Print whether 9 is an element of numbers

print(9 in numbers)

