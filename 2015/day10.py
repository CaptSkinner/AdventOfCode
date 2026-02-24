input = "33113322113"
# "Look-and-say" 40 iterations
# if not repeated + 1n
# if repeated + t_repeated+n

def get_las(input):
    output = ""
    for number in range(len(input)):
        if input[number] == input[number]:
            output += "2" + input[number]
            number + 2
        else:
            output += input[number]
            number + 1

        print(output)






get_las(input)


