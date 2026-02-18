## Work in Progress

file = "../Inputs/day7.txt"
with open(file, 'r') as file:
    instructions = file.read()
print(instructions.split("\n"))
print(instructions.split("\n")[0].split(" "))

# Examples
# if "AND" in instructions:
#     destination = source1 & source2
# if "OR" in instructions:
#     destination = source1 | source2
# if "LSHIFT" in instructions:
#     destination = source1 << amount
# if "RSHIFT" in instructions:
#     destination = source1 >> amount
# if "NOT" in instructions:
#     destination = ~source1 & 0xFFFF

