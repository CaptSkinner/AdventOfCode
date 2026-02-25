# WIP only working with a single digit on the end
# need to add guardrail for the index out of range
input = "3113322113"

def get_las(input):
    output = []
    index = 0
    counter = 1
    while index + 1 < len(str(input)):
        while input[index] == input[index + 1]:
            counter += 1
            index += 1
        output.append(str(counter) + input[index])
        index += 1
        counter = 1
    output.append(str(counter) + input[index])
    return "".join(output)

print(get_las(input))