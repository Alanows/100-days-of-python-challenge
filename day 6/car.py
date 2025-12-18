class Car:
    def __init__(self,make,model,year,tank):
        self.make = make
        self.model = model
        self.year = year
        self.odometor_reading = 0
        self.level_tank = tank
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"your car has a total of {self.odometor_reading} miles")
    
    def update_odometer(self,mileage):
        self.odometor_reading = mileage
        
    def increment_odometer(self,miles):
        self.odometor_reading += miles
    
    def fill_gas_tank(self):
        print(f"this car has a {self.level_tank} in the tank")

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size
    
    def describe_battery(self, update_size = None):
        if update_size is not None:
            self.battery_size = update_size
        print(f"this car has a {self.battery_size}--kwh battery")
        
        
    def upgrade_battery(self):
        if self.battery_size == 100:
            print("your battery is already full")
        else:
            self.battery_size = 100
            print(f"we recharged your battery to full, now is {self.battery_size}")
    
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size  == 100:
            range = 315
        else:
            range = 0
        
        print(f"This car can go about {range} miles on a full charge.")
        
    
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year,tank=0)
        self.battery = Battery()

    
    def fill_gas_tank(self):
        print("this card doesn't need a gas tank!")

"""
#create car ---------------------------------------------
non_tesla = Car('tesla','model s','2019',50)
my_tesla = ElectricCar('tesla','model s','2019')
print("---------------------------------------------")
print(my_tesla.get_descriptive_name())

#checking if the car is electric car or not -------------
print("---------------------------------------------")
non_tesla.fill_gas_tank()
my_tesla.fill_gas_tank()

# checking battery problemes ----------------------------
print("---------------------------------------------")
my_tesla.battery.describe_battery(43)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

"""


