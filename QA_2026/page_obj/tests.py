from page import LoginPage
import json
 
path = "QA_2026/page_obj/test_data.json"
with open(path) as file:
    strObj = file.read()
    data = json.loads(strObj)
    print("Usernaem: ", data["username"], "\nPassword: ", data["password"])
    page = LoginPage()
    page.login(data["username"], data["password"])