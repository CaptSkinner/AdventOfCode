file = "../Inputs/day6.txt"
with open(file, 'r') as file:
    lights_grid = file.read()

#get starting grid of lights
lights_grid_status = [[0 for lights in range(1000)] for lights in range(1000)]

lights_grid = lights_grid.split("\n")

for lights in lights_grid:
    # split up instructions
    instructions = lights.split(" ")

    # Get Starting locations
    start_x, start_y = instructions[-3].split(",")

    # Get Finishing locations
    finish_x, finish_y = instructions[-1].split(",")

    # what to do with lights
    on_off_toggle = instructions[-4]

    # Toggle lights in xy ranges
    for x in range(int(start_x), int(finish_x) + 1):
        for y in range(int(start_y), int(finish_y) + 1):
            if lights_grid_status[x][y] >= 0:
                # Add brightness by 1
                if on_off_toggle == "on":
                    lights_grid_status[x][y] += 1
                # Decrease brightness by 1
                elif on_off_toggle == "off":
                    lights_grid_status[x][y] -= 1
                    # catch event that brightness goes below 0
                    if lights_grid_status[x][y] < 0:
                        lights_grid_status[x][y] = 0
                # Increase brightness by 2
                elif on_off_toggle == "toggle":
                    lights_grid_status[x][y] += 2

print(lights_grid_status)
#Count number of On lights
brightness = 0
for row in lights_grid_status:
    brightness += sum(row)

print(f"The brightness is {brightness}")

