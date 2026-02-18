file = "../Inputs/day5.txt"
with open(file, 'r') as file:
    nice_strings = file.read()

nice_list_count = 0
nice_strings = nice_strings.split("\n")

for strings in nice_strings:
    # Check for paired strings repeateds
    has_paired = False
    for letter in range(len(strings) - 1):
        pair = strings[letter:letter + 2] # grabs a pair of letters
        if pair in strings[letter+2:]: has_paired = True # checks if pair matches from the start to the end of the string

    # Check if paired strings have 1 letter between them
    paired_between_1 = False
    for letter in range(len(strings) - 2 ):
        if strings[letter] == strings[letter + 2]: paired_between_1 = True # checks if letter 0 and letter 2 match, along the line

    # if both conditions are met
    if has_paired and paired_between_1: nice_list_count += 1
print(nice_list_count)