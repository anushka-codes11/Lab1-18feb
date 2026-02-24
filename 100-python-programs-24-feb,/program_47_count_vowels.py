def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

s = input()
print(count_vowels(s))

// input : 
  Hello World
// otput :
     3