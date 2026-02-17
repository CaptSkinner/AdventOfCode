# Open file
file = "day3.txt"
with open(file, 'r') as file:
    movements = file.read()

# House start location
x, y = 0, 0
house_stops = set()
house_stops.add((x, y))

# Movements
for movement in movements:
    if movement == ">": x += 1
    if movement == "<": x -= 1
    if movement == "^": y += 1
    if movement == "v": y -= 1
    house_stops.add((x, y))

# Amount of unique houses visited
print(len(house_stops))
