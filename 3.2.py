# 1
print("#1")
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item, end=" ")
print()

my_tuple = (10, 20, 30)
for item in my_tuple:
    print(item, end=" ")
print()

my_string = "Hello"
for char in my_string:
    print(char, end=" ")
print()
for i in range(5):  
    print(i, end=" ")
print()

# 2. 
print("#2")
count = 0
while count < 5:
    print("Count:", count, end=" ")
    count += 1
print()

# 3. 
print("#3")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
print()

# 4. 
print("#4")
for i in range(10):
    if i == 5:
        break  
    if i % 2 == 0:
        continue  
    if i == 7:
        pass  
    print(i, end=" ")
print()

# 5
print("#5")
my_list = ["apple", "banana", "cherry"]
for index, fruit in enumerate(my_list):
    print(f"Index: {index}, Fruit: {fruit}")
print()

# 6
print("#6")
for i in range(1, 10, 2): 
    print(i, end=" ") 
print()

# 7
print("#7")
my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}", end=" ")
print()
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}", end=" ") 
print()

# 8
print("#8")
squares = [x**2 for x in range(10)]  
print(squares, end=" ")
print()
even_numbers = [x for x in range(20) if x % 2 == 0]  
print(even_numbers, end=" ")
print()
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened, end=" ")
print()