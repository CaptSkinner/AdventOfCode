file = "../Inputs/day16.txt"
with open(file, 'r') as file:
    aunties = file.read()

wrapping_paper = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse_sues(aunties):
    sues = {}
    for line in aunties.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        sue_idx = line.index(":")
        sue_id = int(line[4:sue_idx])
        props = {}
        for part in line[sue_idx + 1:].split(","):
            key, val = part.strip().split(":")
            props[key.strip()] = int(val.strip())
        sues[sue_id] = props
    return sues


def find_sue_part2(sues, wrapping_paper):
    for sue_id, props in sues.items():
        is_match = True

        for key, val in props.items():
            target = wrapping_paper[key]

            # Special logic for cats and trees (Greater than)
            if key in ["cats", "trees"]:
                if val <= target:
                    is_match = False
                    break

            # Special logic for pomeranians and goldfish (Less than)
            elif key in ["pomeranians", "goldfish"]:
                if val >= target:
                    is_match = False
                    break

            # Exact match for everything else
            else:
                if val != target:
                    is_match = False
                    break

        if is_match:
            return sue_id

    return None


# Then call the new function
sues = parse_sues(aunties)
answer_part2 = find_sue_part2(sues, wrapping_paper)
print(f"Aunt Sue number (Part 2): {answer_part2}")

sues = parse_sues(aunties)
answer = find_sue_part2(sues, wrapping_paper)
print(f"Aunt Sue number: {answer}")
