from prac_09.taxi import Taxi

# Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23
my_taxi = Taxi('Prius 1', 100)
# Drive the taxi 40 km
my_taxi.drive(40)
# Print the taxi's details and the current fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare()}")
