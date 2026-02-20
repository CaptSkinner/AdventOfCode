import time

file = "../Inputs/day8.txt"
with open(file, 'r') as file:
    strings_list = file.read().split("\n")

# Get total literal characters
strings_literal = 0
for string in strings_list:
    strings_literal += len(string)


def count_mem_char(strings_list):
    total_memory = 0
    total_strings = len(strings_list)

    for i, strings in enumerate(strings_list):
        string = strings[1:-1]
        char_count = 0
        index = 0

        while index < len(string):
            time.sleep(.001)
            if string[index] == "\\":
                if string[index + 1] == "\\":
                    char_count += 1
                    index += 2
                elif string[index + 1] == '"':
                    char_count += 1
                    index += 2
                elif string[index + 1] == "x":
                    char_count += 1
                    index += 4
            else:
                char_count += 1
                index += 1

        total_memory += char_count

        # Print progress every 10%
        if (i + 1) % (total_strings // 10) == 0:
            percent = ((i + 1) / total_strings) * 100
            print(f"Progress: {percent:.0f}%")

    return total_memory


strings_memory = count_mem_char(strings_list)
print(f"Literal: {strings_literal}")
print(f"Memory: {strings_memory}")
print(f"Difference: {strings_literal - strings_memory}")