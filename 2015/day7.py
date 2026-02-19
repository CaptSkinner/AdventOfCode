file = "../Inputs/day7.txt"
with open(file, 'r') as file:
    instructions = file.read().split("\n")

wire_diagram = {}

def get_value(input_str):
    if input_str.isdigit():
        return int(input_str)
    else:
        return wire_diagram[input_str]

def install_wires(instructions):
    while instructions:
        remaining = []

        for instruction in instructions:
            parts = instruction.split(" -> ")
            source = parts[0]
            destination = parts[1]

            try:
                if "AND" in source:
                    sources = source.split(" AND ")
                    wire_diagram[destination] = (get_value(sources[0])) & (get_value(sources[1]))

                elif "OR" in source:
                    sources = source.split(" OR ")
                    wire_diagram[destination] = (get_value(sources[0])) | (get_value(sources[1]))

                elif "LSHIFT" in source:
                    parts_op = source.split(" LSHIFT ")
                    wire_diagram[destination] = get_value(parts_op[0]) << int(parts_op[1])

                elif "RSHIFT" in source:
                    parts_op = source.split(" RSHIFT ")
                    wire_diagram[destination] = get_value(parts_op[0]) >> int(parts_op[1])

                elif "NOT" in source:
                    source1 = source.replace("NOT ", "")
                    wire_diagram[destination] = ~(get_value(source1)) & 0xFFFF

                else:
                    val = get_value(source)
                    wire_diagram[destination] = val

            except (KeyError, ValueError):
                remaining.append(instruction)

        instructions = remaining



install_wires(instructions)
print(wire_diagram["a"])
