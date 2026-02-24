# File Name: first_non_repeating.py

# Read input from standard input
input_string = input().strip()

# Dictionary to store frequency of characters
frequency = {}

# Count occurrences
for char in input_string:
    frequency[char] = frequency.get(char, 0) + 1

# Find first non-repeating character
result = -1
for char in input_string:
    if frequency[char] == 1:
        result = char
        break

# Print the required output
print(result)

// input :
programming
// output :
p