file_path = "../Inputs/day17.txt"

with open(file_path, 'r') as f:
    containers = [int(line) for line in f.read().splitlines() if line.strip()]

target_l = 150

def solve_eggnog(containers, target_volume):
    successful_counts = []

    def find_combinations(index, current_target, containers_used):
        if current_target == 0:
            successful_counts.append(containers_used)
            return
        if current_target < 0 or index == len(containers):
            return
        find_combinations(index + 1,
                          current_target - containers[index],
                          containers_used + 1)
        find_combinations(index + 1,
                          current_target,
                          containers_used)

    find_combinations(0, target_volume, 0)

    total_ways = len(successful_counts)

    return total_ways



total_ways = solve_eggnog(containers, target_l)

print(f"Total combinations: {total_ways}")