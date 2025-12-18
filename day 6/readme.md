# Python OOP Practice Project

This repository contains several small Python scripts created to practice **Object-Oriented Programming (OOP)** concepts such as classes, inheritance, composition, and module imports.

## Files Overview

### `car.py`
Defines the core classes for vehicles:
- **Car**: Represents a gas-powered car with attributes like make, model, year, odometer, and gas tank level.
- **Battery**: Represents a battery for electric cars, with methods to describe, upgrade, and calculate range.
- **ElectricCar**: Inherits from `Car` and uses a `Battery` object instead of a gas tank.

This file is the base module used by other scripts.

---

### `electric_car.py`
Separates electric car logic into its own module:
- Imports `Car` from `car.py`.
- Defines **Battery** and **ElectricCar** classes.

This demonstrates how to split classes into different files and reuse them using imports.

---

### `my_car.py`
Example usage of the `Car` class:
- Creates a car instance.
- Updates and increments the odometer.
- Prints descriptive information about the car.

Used mainly to test and demonstrate the `Car` class.

---

### `my_cars.py`
Demonstrates working with multiple car types:
- Creates a regular `Car`.
- Creates an `ElectricCar` (imported with an alias).
- Prints descriptive names for both.

Shows inheritance and module aliasing.

---

### `my_electric_car.py`
Focuses on electric car features:
- Creates an `ElectricCar` instance.
- Modifies battery size.
- Checks driving range.
- Upgrades the battery.

Demonstrates composition (a car *has a* battery).

---

### `printing_models.py`
Demonstrates importing functions from another module:
- Imports `make_pizza` from `printin_functions` using an alias.
- Passes a list of pizzas to the function.

Shows how to import and rename functions from external files.

---

### `restaurantes.py`
Practices inheritance with a restaurant example:
- **Restaurant**: Base class with restaurant information and customer tracking.
- **IceCreamTruck**: Child class that adds ice cream flavors.

At the end of the file, objects are created and methods are executed.

---

### `prueba.py`
Simple test script:
- Imports the `Privilegios` class from a `usuario` module.
- Creates an instance and displays privileges.

Used to test external class imports.

---

## Concepts Practiced
- Classes and objects
- Inheritance
- Composition
- Method overriding
- Importing modules and classes
- Aliasing imports

## Purpose
This project is intended for **learning and practicing Python OOP fundamentals**, commonly taught in beginner to intermediate Python courses.

