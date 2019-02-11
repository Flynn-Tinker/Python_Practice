import sys

MASTER_PASSWORD = "opensesame"
password = input("Please input password: ")
attempt_count = 1

while password !=  MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many attempts")
    password= input("Invalid password, try again: ")
    attempt_count += 1
    print(attempt_count)
print("Welcome")
