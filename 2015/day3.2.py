file = "day3.txt"
with open(file, 'r') as file:
    movements = file.read()

#Santa
x, y = 0, 0
santas_house_stops = set()
santas_house_stops.add((x, y))

#Robo_Santa
a, b, = 0, 0
robo_santas_stops = set()
robo_santas_stops.add((a, b))

#eggnoggedly movements
for index, movement in enumerate(movements):
    if index % 2 == 0:
        if movement == ">": x += 1
        elif movement == "<": x -= 1
        elif movement == "^": y += 1
        elif movement == "v": y -= 1
        santas_house_stops.add((x, y))
    else:
        if movement == ">": a += 1
        elif movement == "<": a -= 1
        elif movement == "^": b += 1
        elif movement == "v": b -= 1
        robo_santas_stops.add((a, b))

all_stops = santas_house_stops | robo_santas_stops
print(len(all_stops))


