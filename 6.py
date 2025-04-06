# Import arithmetic module
import arithmetic_module as am

print(am.is_even_or_odd(10))  
print()  

print(am.add_ab(10, 5))  

# %%
# Import datetime and time separately
from datetime import datetime
import time  

# Print current datetime
now = datetime.now()  
print(now)  

# Wait for 5 seconds
time.sleep(5)  

# Print updated datetime
now = datetime.now()  
print(now)  

print()
print("Year  :", now.year)  
print("Month :", now.month)  
print("Day   :", now.day)  
print("Hour  :", now.hour)  
print("Minute:", now.minute)  
print("Second:", now.second)  

# %%
# Import area and prime module
import area_prime_module as apm  

print("7 is  :", apm.is_prime(7))  
print("10 is :", apm.is_prime(10))  

# Calculate area of different shapes
circle_area = apm.Circle.area(5)  
print("Circle Area     :", circle_area)  

rectangle_area = apm.Rectangle.area(15, 20)  
print("Rectangle Area  :", rectangle_area)  

triangle1_area = apm.Triangle.area(5, 10)  
print("Triangle1 Area  :", triangle1_area)  

triangle2_area = apm.Triangle.area(3, 4, 5)  
print("Triangle2 Area  :", triangle2_area)  
