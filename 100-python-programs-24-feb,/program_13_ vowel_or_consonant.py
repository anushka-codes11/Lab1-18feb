# Read a single character from standard input
char = input().strip()

# Check if input is a single alphabet
if len(char) == 1 and char.isalpha():
    # Convert to lowercase for uniformity
    ch = char.lower()
    
    # Check vowel or consonant
    if ch in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid Input")

// input :  
   a 
// output:
   vowel        