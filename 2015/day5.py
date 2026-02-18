file = "../Inputs/day5.txt"
with open(file, 'r') as file:
    nice_strings = file.read()

nice_list_count = 0
vowels = ["a", "e", "i", "o", "u"]
bad_strings = ["ab", "cd", "pq", "xy"]
nice_strings = nice_strings.split("\n")

for strings in nice_strings:
    # Check for bad strings
    has_bad_string = False
    for bad in bad_strings:
        if bad in strings:
            has_bad_string = True
            break
    if has_bad_string:
        continue

    # Check for double letters
    has_double = False
    for double in range(len(strings) - 1):
        if strings[double] == strings[double + 1]:
            has_double = True
            break

    # Count vowels
    vowel_count = 0
    for letter in strings:
        if letter in vowels:
            vowel_count += 1

    # add to nice list if conditions are met
    if has_double and vowel_count >= 3:
        nice_list_count += 1

print(nice_list_count)