# Work in Progress

file = "../Inputs/day8.txt"
with open(file, 'r') as file:
    string_literals = file.read().split("\n")

# get total amount of characters
strings_count = 0
for strings in string_literals:
    strings_count += len(strings)

# get alpha characters len only
character_only_list = []
for strings in string_literals:
    for letters in strings:
        if letters.isalpha():
            character_only_list.append(letters)




print(f"strings_count = {strings_count}")
print(string_literals)
print()
print(f"character_only_list = {character_only_list}")
print(print(f"character_only_list length = {len(character_only_list)}"))