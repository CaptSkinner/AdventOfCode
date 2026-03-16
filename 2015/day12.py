import json

file_path = "../Inputs/day12.json"
with open(file_path, 'r') as f:
    books = json.load(f)

def calc_sum(data):
    total = 0
    # recurse over lists, add to total
    if isinstance(data, list):
        for item in data:
            total += calc_sum(item)
    # recurse over dict, add to total
    elif isinstance(data, dict):
        # If value "red" do not count that dict
        if "red" in data.values():
            return 0
        for val in data.values():
            total += calc_sum(val)
    # if int or float, add to total
    elif isinstance(data, (int, float)):
        total += data
    return total

result = calc_sum(books)
print(result)
