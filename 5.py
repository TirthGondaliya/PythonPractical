# Base class for demonstrating polymorphism
class Vehicle:
    def move(self):
        pass  # Method to be overridden

# Subclasses implementing polymorphism
class Car(Vehicle):
    def move(self):
        return "Drive"

class Bike(Vehicle):
    def move(self):
        return "Ride"

# Encapsulation: Private attributes with getter and setter methods
class Owner:
    def __init__(self, name, age):
        self._name = name  # Private attribute
        self._age = age    # Private attribute
    
    @property
    def name(self):
        return self._name  # Getter method
    
    @name.setter
    def name(self, new_name):
        self._name = new_name  # Setter method
    
    @property
    def age(self):
        return self._age  # Getter method
    
    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self._age = new_age  # Setter method with validation

# Method overriding: Driver class extends Owner
class Driver(Owner):
    def __init__(self, name, age, license_number):
        super().__init__(name, age)
        self.license_number = license_number  # Additional attribute

# Method overloading simulation using default arguments
class SpeedCalculator:
    def calculate_speed(self, distance, time, factor=1):
        return (distance / time) * factor  # Handles different cases

# Class method to operate on class-level data
class VehicleCounter:
    count = 0  # Class-level attribute
    
    def __init__(self):
        VehicleCounter.count += 1  # Increment count on instance creation
    
    @classmethod
    def get_count(cls):
        return cls.count  # Returns total instances created

# Static method for utility function
class Utility:
    @staticmethod
    def is_fast(speed):
        return speed > 60  # Checks if speed is above a threshold

# Testing the code
if __name__ == "__main__":
    # Demonstrating polymorphism
    print(Car().move())  # Output: Drive
    print(Bike().move())  # Output: Ride
    
    # Testing encapsulation
    owner = Owner("Alice", 30)
    print(owner.name)  # Output: Alice
    
    # Testing method overriding
    driver = Driver("Bob", 40, "DL12345")
    print(driver.name, driver.age, driver.license_number)  # Output: Bob 40 DL12345
    
    # Testing method overloading
    speed_calc = SpeedCalculator()
    print(speed_calc.calculate_speed(100, 2))  # Output: 50.0
    print(speed_calc.calculate_speed(100, 2, 1.1))  # Output: 55.0
    
    # Testing class method
    print(VehicleCounter.get_count())  # Output: Number of instances created
    
    # Testing static method
    print(Utility.is_fast(70))  # Output: True
    print(Utility.is_fast(50))   # Output: False