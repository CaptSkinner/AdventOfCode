# Part 1 completed

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

min_dist = 999999999
def find_shortest(current_path, remaining_cities):
    global min_dist

    if not remaining_cities:
        this_trip_dist = 0
        for i in range(len(current_path) - 1):
            city_a = current_path[i]
            city_b = current_path[i + 1]
            this_trip_dist += flights_array[city_a][city_b]

        if this_trip_dist < min_dist:
            min_dist = this_trip_dist


    for path in range(len(remaining_cities)):
        next_city = remaining_cities[path]
        new_remaining = remaining_cities[:path] + remaining_cities[path + 1:]

        find_shortest(current_path + [next_city], new_remaining)



find_shortest([], list(city_list))
print(min_dist)












