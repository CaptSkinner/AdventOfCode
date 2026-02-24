#WIP

file = "../Inputs/day9.txt"
with open(file, 'r') as file:
    routes = file.read().split("\n")

flights_array = {}
city_list = set()

for route in routes:
    # capture flight routes
    flight = [route.split(" = ")[0]]
    # capture flight distance
    distance = int(route.split(" = ")[1])

    for destinations in flight:
        # capture departure and destination cities
        departure = str(destinations.split(" to ")[0])
        destination = str(destinations.split(" to ")[1])
        # build city total city list
        city_list.add(departure)
        city_list.add(destination)

        # building dict keys for flight array
        if departure not in flights_array:
            flights_array[departure] = {}
        if destination not in flights_array:
            flights_array[destination] = {}

        # populating flight array and total city list
        flights_array[departure][destination] = distance
        flights_array[destination][departure] = distance
        city_list.add(departure)
        city_list.add(destination)

print(flights_array)













