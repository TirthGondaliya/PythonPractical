def divide(a, b):
    try:
        # 1 Use a try-except block to catch and handle exceptions.
        result = a / b  # This might raise a ZeroDivisionError
    except ZeroDivisionError:
        # 2 Use multiple except blocks to handle different types of exceptions.
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input type. Please enter numbers.")
    else:
        # 3 Use an else block to execute code if no exceptions are raised.
        print("Division successful! Result:", result)
    finally:
        # 4 Use a finally block to execute code regardless of whether an exception is raised.
        print("Execution completed.")

# Function calls
divide(10, 2)  
divide(10, 0)  
divide(10, "a")  

# 5 Use the raise statement to raise an exception manually.
def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old.")  # Raising an exception manually
    print("Access granted.")

# Exception handling for check_age function
try:
    check_age(15)  # This will raise an exception
except ValueError as e:
    print("Exception:", e)  # Handling the raised exception
