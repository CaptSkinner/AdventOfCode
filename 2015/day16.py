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

def find_sue(sues, wrapping_paper):
    for sue_id, props in sues.items():
        if all(wrapping_paper.get(k) == v for k, v in props.items()):
            return sue_id
    return None

sues = parse_sues(aunties)
answer = find_sue(sues, wrapping_paper)
print(f"Aunt Sue number: {answer}")
