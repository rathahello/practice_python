# import json

path = "data.txt"
with open(path) as file:
    print(file.read())


data = {
    "username": "admin",
    "password": "123456"
}

try:
    num = int(input("enter number..."))
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
except ValueError:
    print("Error")

print(data["username"])