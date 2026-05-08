# File Name: remove_duplicates.py

# Read input from standard input
input_string = input().strip()

# Remove duplicate characters while preserving order
result = ""
seen = set()

for char in input_string:
    if char not in seen:
        seen.add(char)
        result += char

# Print the required output
print(result)

//input :
programming
// output : 
progamin