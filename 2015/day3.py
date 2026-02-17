file = "day3.txt"
with open(file, 'r') as file:
    movements = file.read()

# house_location
x, y = 0, 0
house_stops = set()
house_stops.add((x, y))

for movement in movements:
    if movement == ">":
        x += 1
    if movement == "<":
        x -= 1
    if movement == "^":
        y += 1
    if movement == "v":
        y -= 1
    house_stops.add((x, y))
print(house_stops)
print(len(house_stops))
