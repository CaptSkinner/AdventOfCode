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

race_duration = 2503
distances = calculate_reindeer_distance_no_regex(reindeer, race_duration)

winner_name, winner_dist = max(distances, key=lambda x: x[1])

print(f"The winner is {winner_name} with {winner_dist} km!")


