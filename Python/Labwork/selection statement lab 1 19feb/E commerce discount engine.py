cart = float(input("Enter cart value: "))
member = input("Membership (silver/gold/platinum): ")
festival = input("Festival season? (yes/no): ")

discount = 0

if member == "silver":
    discount = 5
elif member == "gold":
    discount = 10
elif member == "platinum":
    discount = 15

if festival == "yes":
    discount += 5

final_amount = cart - (cart * discount / 100)

print("Final Payable Amount:", final_amount)