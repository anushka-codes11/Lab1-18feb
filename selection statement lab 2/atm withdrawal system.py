balance = int(input("Enter balance: "))
withdraw = int(input("Enter withdrawal amount: "))
atm_cash = int(input("ATM cash available: "))

if withdraw > balance:
    print("Insufficient Balance")
elif withdraw > 50000:
    print("Daily Limit Exceeded")
elif withdraw > atm_cash:
    print("ATM has insufficient cash")
else:
    print("Withdrawal Successful")