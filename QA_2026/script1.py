# arr = ["A839hfqne9a", "Fnfaoinfa", "Cfiajfie", "Dejfi", "Eoueow"]
# arr_id = [12, 34, 55, 32, 25]
# arr_2 = []
# print(arr.count("A839hfqne9a"))
# arr.sort()
# arr.sort(reverse=True)
# arr.reverse()
# arr.remove("A839hfqne9a")
# arr.pop(2) # delete by index
# del arr[2] # delete by index 
# arr_2 = arr.copy() # copy array list
# arr_2 = list(arr) # copy array list
# result = arr + arr_id # combine value in one array
# arr.extend(arr_id) # # combine value in one array
# print(arr)


### Object
# empID = {101, 102, 103, 104, 101}
# names = {"Alex", "Jonh", "Jakson", "Moka"}

# empID.add(200)
# empID.discard(101)
# names.add(301)
# empID.remove(102)
# # del empID
# empID.clear()
# empID.add(300)
# print(empID)

# value = input("Enter studen Name: ")
# if value in names:
#     print(value, " is a student")
# else:
#     print("Not in student lists")
#     names.add(value)
# print("Student Lists: ", names)


### Tuple
# tuple_list = ("testing", 2, 3, 4, 5, 2, 3, 4)
# result = len(tuple_list) # count len in tuple 
# result = tuple_list.count(5) # count how many value in tuple
# result = list(tuple_list)
# result.insert(2, "TEST") # insert any value into tuple by index
# result = tuple(tuple_list[2:3])
# print(result)


### Dictionary
employee = {
    "name": "Jonh Jakson",
    "id": 101,
    "salary": 250000,
    "role": "QA",
    "tasks": {
        "task_001",
        "task_002"
    }
}
print(employee["name"])
# del employee["id"] # remove param from object
# employee["department"] = "IT" # insert new param in object
# result = employee.pop("id")
# get_task = employee["tasks"]
# result = next(iter(task)) # random value
# result = list(get_task)
# print(result[0])