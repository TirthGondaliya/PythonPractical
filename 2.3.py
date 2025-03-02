dict = {1:"Apple", 2:"Berry", 3:"Cherry", 4:"Date", 5:"Elderberry"}
print(dict)

print("Access",dict[1])

dict.update({2:"Banana"})
print("Update",dict)

del dict[2]
print("Delete",dict)

for key in dict.keys():
    print("Keys:",key)

for value in dict.values():
    print("Values:",value)

for key, value in dict.items():
    print(f"{key}: {value}")

dict.popitem()
print("Pop",dict)

nested = {"spell":{1:"one", 2:"two"}, "spell2":{3:"three", 4:"four"}}
print("Nested",nested)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {**dict1, **dict2}
print("Merge",dict3)





