class Car:

    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")        

class ElectricCar(Car):
    "Represent aspects of a car specific to electric vehicles."
    
    def __init__(self, make, model, year):
        "Initialize attributes of the parent class"
        super().__init__(make, model, year)
        self.battery = Battery()
    def increment_odometer(self):
        return "Doesn't need a gas tank"
        
my_tesla = ElectricCar("tesla", 'model s', 2019)
print(my_tesla.increment_odometer())
my_tesla.battery.describe_battery()
# __super__() makes python __init__() from Car class