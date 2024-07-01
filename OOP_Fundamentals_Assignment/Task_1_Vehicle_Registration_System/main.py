# Define the Vehicle class
class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.vehicle_type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to {new_owner}")

# Function to add a vehicle
def add_vehicle(vehicle_list, reg_num, vehicle_type, owner):
    vehicle = Vehicle(reg_num, vehicle_type, owner)
    vehicle_list.append(vehicle)
    print(f"Vehicle {reg_num} added. Model: {vehicle_type}, Owner: {owner}")

# Function to change the vehicle owner
def change_vehicle_owner(vehicle_list, reg_num, new_owner):
    for vehicle in vehicle_list:
        if vehicle.registration_number == reg_num:
            vehicle.update_owner(new_owner)
            return
    print(f"Vehicle with registration number {reg_num} not found.")

# Example usage
vehicle_list = []

# Adding vehicles with creative names and car brands/models
add_vehicle(vehicle_list, "XY123Z", "Tesla Model S", "Elon Musk")
add_vehicle(vehicle_list, "AB456C", "Ford Mustang", "Steve McQueen")
add_vehicle(vehicle_list, "GH789I", "Chevrolet Camaro", "Bumblebee")
add_vehicle(vehicle_list, "JK101L", "Porsche 911", "James Dean")

# Display initial owners
print(f"Initial owner of XY123Z: {vehicle_list[0].owner}")
print(f"Initial owner of AB456C: {vehicle_list[1].owner}")
print(f"Initial owner of GH789I: {vehicle_list[2].owner}")
print(f"Initial owner of JK101L: {vehicle_list[3].owner}")

# Changing vehicle owners
change_vehicle_owner(vehicle_list, "XY123Z", "Tony Stark")
change_vehicle_owner(vehicle_list, "AB456C", "Carroll Shelby")
change_vehicle_owner(vehicle_list, "GH789I", "Optimus Prime")
change_vehicle_owner(vehicle_list, "JK101L", "Paul Walker")

# Display updated owners
print(f"Updated owner of XY123Z: {vehicle_list[0].owner}")
print(f"Updated owner of AB456C: {vehicle_list[1].owner}")
print(f"Updated owner of GH789I: {vehicle_list[2].owner}")
print(f"Updated owner of JK101L: {vehicle_list[3].owner}")

