file = "../Inputs/day6.txt"
with open(file, 'r') as file:
    lights_grid = file.read()

#get starting grid of lights - assuming they're all off?
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
            if on_off_toggle == "on":
                lights_grid_status[x][y] = 1
            elif on_off_toggle == "off":
                lights_grid_status[x][y] = 0
            elif on_off_toggle == "toggle":
                lights_grid_status[x][y] = 1 - lights_grid_status[x][y]



#Count number of On lights
lights_on = 0
for row in lights_grid_status:
    lights_on += sum(row)

print(f"There are {lights_on} lights on")
