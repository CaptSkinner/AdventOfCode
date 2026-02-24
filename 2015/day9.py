#WIP

file = "../Inputs/day9.txt"
with open(file, 'r') as file:
    routes = file.read().split("\n")

flight_array = {}
for route in routes:
    flight = [route.split(" = ")[0]]
    distance = int(route.split(" = ")[1])
    for destinations in flight:
        departure = str(destinations.split(" to ")[0])
        destination = str(destinations.split(" to ")[1])
        flight_array[departure, destination] = distance
        flight_array[destination, departure] = distance







