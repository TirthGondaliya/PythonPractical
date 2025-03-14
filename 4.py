class Car:
    def __init__(self, brand, year):
        self.brand = brand  
        self.year = year

    def details(self):
        return f"Brand:{self.brand}  Year:{self.year}."

    def get_year(self):
        return self.year

    def set_year(self, new_year):
        self.year = new_year

class FuelCar(Car):
    def __init__(self, brand, year, fuel_type):
        super().__init__(brand, year)  
        self.fuel_type = fuel_type
   
    def details(self):
        return f"Brand:{self.brand}  Fuel:{self.fuel_type}  Year:{self.year}"

class City:
    def __init__(self, city_name):
        self.city_name = city_name

    def city(self):
        return f"City:{self.city_name}."


class ElectricCar(FuelCar, City):
    def __init__(self, brand, year, city_name, battery_capacity):
        FuelCar.__init__(self, brand, year, "Electric")
        City.__init__(self, city_name)
        self.battery_capacity = battery_capacity  

    def details(self):
        return f"Brand:{self.brand}  Year:{self.year}  Battery:{self.battery_capacity}" 


car1 = Car("Toyota", 2015)
print(car1.details())

car1.set_year(2020)
print(f"New Year:{car1.get_year()}")

fuel_car1 = FuelCar("TATA", 2018, "Petrol")
print(fuel_car1.details())

electric_car1 = ElectricCar("Suzuki", 2022, "Mumbai", 75)
print(electric_car1.details())
print(electric_car1.city())
