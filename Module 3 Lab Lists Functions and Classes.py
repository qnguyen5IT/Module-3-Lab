"""
-Quang Nguyen
-Module 3 Lab Lists Functions and Classes
-This program takes user's input of the Vehicle, including the year, make, model, type of doors(2 or 4 doors), and roof(solid or sun roof)
"""

# Defining a class called Vehicle
class Vehicle:
    # __init__ method to initializes the class with attribute vehicle_type
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Defining Automobile class, and Automobile class will inherits from Vehicle class
class Automobile(Vehicle):
    # __init__ initializes Automobile class with atributes year, make, model, doors, roof. 
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # super().__init__(vehicle_type) calls constructor of Vehicle class to initialize vehicle_type attribute
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# main function prompts user to enter car's details
def main():
    print("Enter details for your car:")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")
    # Inputs is used for Automobile class
    car = Automobile("car", year, make, model, doors, roof)

    print("\nVehicle Information:")
    print(f"Vehicle type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")

# main fucntion will be called 
if __name__ == "__main__":
    main()
