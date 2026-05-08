# File Name: count_upper_lower.py

# Read input from standard input
input_string = input().strip()

# Initialize counters
uppercase_count = 0
lowercase_count = 0

# Count uppercase and lowercase letters
for char in input_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

# Print the required output
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)

// input :
Hello World! 123
// output:
Uppercase letters: 2
Lowercase letters: 8