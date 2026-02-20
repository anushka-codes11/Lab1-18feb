heart = input("Heart rate abnormal? (yes/no): ")
injury = input("Severe injury? (yes/no): ")
age = int(input("Enter age: "))

if heart == "yes" or injury == "yes":
    print("Critical")
elif age > 65:
    print("Moderate - Priority Upgraded")
else:
    print("Normal")