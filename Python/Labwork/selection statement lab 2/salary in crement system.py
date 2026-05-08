rating = int(input("Performance rating (1-5): "))
experience = int(input("Years of experience: "))
attendance = int(input("Attendance %: "))

if rating >= 4 and experience >= 5 and attendance >= 90:
    print("Increment: 15%")
elif rating >= 3:
    print("Increment: 10%")
else:
    print("Increment: 5%")