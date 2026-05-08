income = float(input("Enter your income: "))
age = int(input("Enter your age: "))

if age >= 60:
    exemption = 300000
else:
    exemption = 250000

if income <= exemption:
    print("No Tax")
elif income <= 500000:
    print("Tax = 5%")
elif income <= 1000000:
    print("Tax = 20%")
else:
    print("Tax = 30%")