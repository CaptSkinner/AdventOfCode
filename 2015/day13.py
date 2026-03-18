file = "../Inputs/day13.txt"
with open(file, 'r') as file:
    seating = file.read()

import re

def parse_happiness(text):
    happiness = {}
    for line in text.splitlines():
        m = re.match(r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.", line)
        if m:
            person, direction, amount, neighbour = m.groups()
            happiness[(person, neighbour)] = int(amount) * (1 if direction == "gain" else -1)
    return happiness


def get_permutations(items):
    if len(items) <= 1:
        return [items]
    result = []
    for i, item in enumerate(items):
        rest = items[:i] + items[i+1:]
        for perm in get_permutations(rest):
            result.append([item] + perm)
    return result


def score_arrangement(arrangement, happiness):
    n = len(arrangement)
    return sum(
        happiness.get((arrangement[i], arrangement[(i + 1) % n]), 0) +
        happiness.get((arrangement[(i + 1) % n], arrangement[i]), 0)
        for i in range(n)
    )


def find_optimal(happiness, extra_people=None):
    people = list({p for p, _ in happiness})
    if extra_people:
        people += extra_people
    anchor, rest = people[0], people[1:]
    best_score, best_arrangement = None, None
    for perm in get_permutations(rest):
        arrangement = [anchor] + perm
        score = score_arrangement(arrangement, happiness)
        if best_score is None or score > best_score:
            best_score, best_arrangement = score, arrangement
    return best_score, best_arrangement


happiness = parse_happiness(seating)

score, arrangement = find_optimal(happiness, extra_people=["Me"])
print(score)