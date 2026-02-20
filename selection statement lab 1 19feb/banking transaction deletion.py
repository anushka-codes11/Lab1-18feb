amount = float(input("Enter transaction amount: "))
account_age = int(input("Enter account age (months): "))
international = input("Is it international? (yes/no): ")

if amount > 200000 and account_age < 6 and international == "yes":
    print("Transaction Flagged for Verification")
else:
    print("Transaction Normal")