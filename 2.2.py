int_list = [2, 4, 6, 8 ,10]
string_list = ["apple", "banana", "cherry", "date"]
mixed_list = [3, "car", 6, "bike"]

print("Access",int_list[2])

print("slice",string_list[0:2])
print("slice",string_list[:4])
print("slice",string_list[3:])

int_list[2] = 5
print("update",int_list)
string_list[2] = "berry"
print("update",string_list)

int_list.append(12)
print("append",int_list)

string_list.insert(2,"blueberry")
print("insert",string_list)

int_list.remove(5)
print("remove",int_list)

pop1 = string_list.pop(2)
print("pop",string_list)

newlist = [1, 3, 5, 7, 9]
conclist = newlist + int_list
print("concatenate",conclist)

replist = mixed_list * 4
print("repeat",replist)

sqlist = [i**2 for i in int_list]
print("square", sqlist)

int_list.sort()
print("sort",int_list)

int_list.reverse()
print("reverse",int_list)

copylist = int_list.copy()
print("copy",copylist)



                                                    

