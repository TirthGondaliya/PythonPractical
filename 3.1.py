# 1
print("#1")
def fun1():
    print("hello")
fun1()
print()

#2
print("#2")
def example_function(positional_arg, default_arg='default', *args, **kwargs):
    print(f"Positional argument: {positional_arg}")
    print(f"Default argument: {default_arg}")
    
    print("Variable-length positional arguments (*args):")
    for arg in args:
        print(arg)
    
    print("Variable-length keyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function('positional', 'default_set', 'extra1', 'extra2', key1='value1', key2='value2')
print()

#3
print("#3")
def calculate(a, b):
    sum_val = a + b
    diff_val = a - b
    prod_val = a * b
    div_val = a / b if b != 0 else None
    
    return sum_val, diff_val, prod_val, div_val

results = calculate(10, 5)
print(results)  
print()


#4
print("#4")
multiply = lambda x, y: x * y
print(multiply(3, 4))  
print()


#5
print("#5")
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(add_five(10))  
print()


#6
print("#6")
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
print()


#7
print("#7")
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
print()


#8
print("#8")
def apply_function(func, value):
    return func(value)



print(apply_function(lambda x:x*x, 5))  
print()


#9
print("#9")
def greet(name):
    """hello"""
    return f"Hello, {name}!"

print(greet.__doc__)
print()


#10
print("#10")
def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(3, 5))