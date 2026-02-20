correct_user = "admin"
correct_pass = "1234"

attempts = 0

while attempts < 3:
    user = input("Username: ")
    password = input("Password: ")
    
    if user == correct_user and password == correct_pass:
        print("Login Successful")
        break
    else:
        print("Wrong Credentials")
        attempts += 1

if attempts == 3:
    print("Account Locked")