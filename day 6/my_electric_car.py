from car import ElectricCar as EC
my_tesla = EC('tesla','model s','2019')
my_tesla.battery.describe_battery(43)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
