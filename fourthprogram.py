# dictionary = pair type key value means (word meaning) , unordered , changeable , dont allow duplicate keys. Dictionary syntax is {}.
# info = {
#     "key" : "value",
#     "name" : "Adarsh Dwivedi",
#     "Learning" : "Coding",
#     "age" : 22,
#     "is_adult" : True,
#     "marks" : 12.96
# }
# print(info["name"])
# print(info["Learning"])
# print(info["age"])
# print(info["marks"])

# info["name"] = "Adarsh"
# info["surname"] = "Dwivedi"
# print(info) 

# Nested Dictionary

# student = {
#     "name" : "Adarsh Dwivedi",
#     "Subjects" : {
#         "maths" : 95,
#         "web tech" : 99,
#         "os" : 98
#     }
# }
# new_dict = {"city" : "chhattisgarh"}
# student.update(new_dict)
# print(student)
# print(student["Subjects"]["os"])
# print(student.keys())
# print(len(list(student.keys())))
# print(list(student.keys()))
# print(student.values())
# print(list(student.items()))
# pairs = list(student.items())
# print(pairs[1])

# SET = Set is a mutable (changeable)in sets only unique value store means set is a collection of unordered lists. its element is unchangeable(immutable).they read duplicate value only 1 time. Set syntax is ().
# collection = {1 ,2, 3, 4, "hello", "world", "hello" , "Adarsh", 5, 7}
# print(collection)
# print(type(collection))
# print(len(collection))

# collection = set()
# collection.add(1)
# collection.add(1)
# collection.add(2)
# collection.add("Adarsh Dwivedi")
# collection.add((1, 2, 3))

# collection.clear()
# print(len(collection))

# print(type(collection))

# collection = {"hello", "apna college", "world", "coding", "python"}

# print(collection.pop())
# print(collection.pop()) #random value pick karta hai

# set1 = {1, 2, 3,6}
# set2 = {2, 5, 6}

# print(set1.union(set2))# combine both set value and return new value
# print(set1)
# print(set1.intersection(set2))# common value comming

