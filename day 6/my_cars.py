from car import Car 
from electric_car import ElectricCar as EC

my_beetle = Car("volwagen",'beetle',2019,40)
print(my_beetle.get_descriptive_name())

my_tesla = EC("tesla",'roadster',2021)
print(my_tesla.get_descriptive_name())