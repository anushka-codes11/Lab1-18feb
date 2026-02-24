# Read marks from standard input
marks = float(input())

# Assign grade based on marks
if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks < 90:
    print("Grade: B")
elif 70 <= marks < 80:
    print("Grade: C")
elif 60 <= marks < 70:
    print("Grade: D")
elif 50 <= marks < 60:
    print("Grade: E")
elif 0 <= marks < 50:
    print("Grade: F")
else:
    print("Invalid Marks") 

// input: 
   85
// output:
   Grade :B 