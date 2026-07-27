# import json

path = "QA_2026/data.txt"
with open(path) as file:
    print(file.read())


data = {
    "username": "admin",
    "password": "123456"
}

try:
    num = input("enter number...")
    if(num > 0):
        print("Positive number")
    elif(num < 0):
        print("Negative number")
except:
    print("Error")

print(data["username"])