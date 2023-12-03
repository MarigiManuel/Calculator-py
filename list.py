"""
numbers = [1, 2, 34, 32, 21, 23]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
"""

"""
numbers = [5, 2, 8, 1, 9, 4]

max_number = max(numbers)

print(f"The maximum number in the list is: {max_number}")

"""

"""
numbers = [2, 5, 7, 8, 9, 2, 4, 2, 4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

"""
original_list = [1, 2, 2, 3, 4, 4, 5]

# Convert the list to a set to remove duplicates
unique_set = set(original_list)

# Convert the set back to a list
unique_list = list(unique_set)

print(unique_list)
















