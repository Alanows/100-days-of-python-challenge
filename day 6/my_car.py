from car import Car
increment = 50

my_new_car = Car('honda','hr-v','2021',89)
print(my_new_car.get_descriptive_name())

my_new_car.odometor_reading = increment
my_new_car.read_odometer()

my_new_car.increment_odometer(increment)
my_new_car.read_odometer()