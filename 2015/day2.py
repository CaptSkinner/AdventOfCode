file = "day2.txt"
with open(file, 'r') as file:
    presents = file.read()

paper_needed = 0
total_ribbon = 0
for present in presents.split("\n"):
    if present:
        l, w, h = map(int, present.split("x"))
        side1, side2, side3,  = l * w, w * h, h * l
        paper_needed += ((side1 + side2 + side3) * 2) + min(side1, side2, side3)
        smallest_sides = sorted([l, w, h])[:2]
        ribbon = ((smallest_sides[0] + smallest_sides[1]) * 2) + (l * w * h)
        total_ribbon += ribbon
print(f"total paper {paper_needed}")
print(f"total ribbon {total_ribbon}")




