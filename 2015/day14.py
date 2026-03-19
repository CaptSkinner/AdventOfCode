file = "../Inputs/day14.txt"
with open(file, 'r') as file:
    reindeer = file.read()


def calculate_reindeer_distance_no_regex(data, race_duration):
    results = []
    reindeers = data.strip().split('\n')
    for reindeer in reindeers:
        words = reindeer.split()

        name = words[0]
        speed = int(words[3])
        fly_time = int(words[6])
        rest_time = int(words[13])

        flight_cycle = fly_time + rest_time
        full_cycles = race_duration // flight_cycle
        remaining_seconds = race_duration % flight_cycle

        total_flying_seconds = (full_cycles * fly_time) + min(fly_time, remaining_seconds)

        distance = total_flying_seconds * speed
        results.append((name, distance))

    return results


def calculate_reindeer_points(data, race_duration):
    reindeers = []

    for lines in data.strip().split('\n'):
        reindeer = lines.split()
        reindeers.append({
            "name": reindeer[0],
            "speed": int(reindeer[3]),
            "fly_limit": int(reindeer[6]),
            "rest_limit": int(reindeer[13]),
            "distance": 0,
            "points": 0
        })

    for second in range(1, race_duration + 1):
        for r in reindeers:
            cycle_time = r["fly_limit"] + r["rest_limit"]

            if 0 < (second % cycle_time) <= r["fly_limit"]:
                r["distance"] += r["speed"]

        lead_distance = max(r["distance"] for r in reindeers)

        for r in reindeers:
            if r["distance"] == lead_distance:
                r["points"] += 1

    return reindeers


race_duration = 2503
distances = calculate_reindeer_distance_no_regex(reindeer, race_duration)
final_stats = calculate_reindeer_points(reindeer, race_duration)

winner_name, winner_dist = max(distances, key=lambda x: x[1])
winner = max(final_stats, key=lambda x: x["points"])

print(f"The winner is {winner_name} with {winner_dist} km!")
print(f"The winner by points is {winner['name']} with {winner['points']} points!")

