username = "admin"
password = "1234"

print("LOGIN")

while True:
    u = input("Username: ")
    p = input("Password: ")

    if u == username and p == password:
        print("Logged in!")
        break
    else:
        print("Incorrect. Try again.")
