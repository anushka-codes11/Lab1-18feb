percentage = float(input("Enter 12th percentage: "))
maths = input("Studied Mathematics? (yes/no): ")
exam = int(input("Entrance exam score: "))

if percentage < 75:
    print("Not Eligible: Less than 75%")
elif maths != "yes":
    print("Not Eligible: Mathematics required")
elif exam < 80:
    print("Not Eligible: Entrance score less than 80")
else:
    print("Eligible for Admission")