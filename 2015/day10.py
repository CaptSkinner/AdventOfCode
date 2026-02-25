input = "3113322113"

def get_las(input):
    output = []
    index = 0
    counter = 1
    while index + 1 < len(input):
        if input[index] == input[index + 1]:
            counter += 1
            index += 1
        else:
            output.append(str(counter) + input[index])
            index += 1
            counter = 1
    output.append(str(counter) + input[index])
    return "".join(output)

result = input
for attempts in range(50):
    result = get_las(result)

print(len(result))