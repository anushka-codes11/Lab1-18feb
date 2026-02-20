units = int(input("Enter units: "))
senior = input("Senior citizen? (yes/no): ")

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

if senior == "yes":
    bill = bill * 0.9   # 10% discount

print("Total Bill:", bill)