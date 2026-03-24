file_path = "../Inputs/day17.txt"

with open(file_path, 'r') as f:
    containers = [int(line) for line in f.read().splitlines() if line.strip()]

target_l = 150


def solve_eggnog_part2(containers, target_volume):
    successful_counts = []

    def find_combinations(index, current_target, containers_used):
        if current_target == 0:
            successful_counts.append(containers_used)
            return
        if current_target < 0 or index == len(containers):
            return

        find_combinations(index + 1, current_target - containers[index], containers_used + 1)
        find_combinations(index + 1, current_target, containers_used)

    find_combinations(0, target_volume, 0)

    if not successful_counts:
        return 0, 0

    min_containers = min(successful_counts)

    ways_to_fill_min = successful_counts.count(min_containers)

    return min_containers, ways_to_fill_min


min_qty, min_ways = solve_eggnog_part2(containers, target_l)

print(f"Minimum number of containers: {min_qty}")
print(f"How many different ways can you fill {min_qty} containers? {min_ways}")