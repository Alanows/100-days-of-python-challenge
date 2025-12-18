from car import Car

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