file = "../Inputs/day15.txt"
with open(file, 'r') as file:
    ingredients_params = file.read()


def parse_ingredients(input_text):
    ingredients = []
    for line in input_text.strip().split('\n'):
        # Parse line like: "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8"
        name, properties = line.split(': ')
        props = {}
        for prop in properties.split(', '):
            key, value = prop.split()
            props[key] = int(value)
        ingredients.append((name, props))
    return ingredients


def calculate_score(amounts, ingredients, check_calories=True, target_calories=500):
    properties = ['capacity', 'durability', 'flavor', 'texture']
    totals = {prop: 0 for prop in properties}
    total_calories = 0

    # Sum up each property across all ingredients
    for amount, (name, props) in zip(amounts, ingredients):
        for prop in properties:
            totals[prop] += amount * props[prop]
        total_calories += amount * props['calories']

    # If checking calories and it doesn't match target, return 0
    if check_calories and total_calories != target_calories:
        return 0

    # Negative totals become 0
    for prop in properties:
        if totals[prop] < 0:
            totals[prop] = 0

    # Multiply all properties together (except calories)
    score = 1
    for prop in properties:
        score *= totals[prop]

    return score


def find_best_cookie(ingredients, total_teaspoons=100, check_calories=True, target_calories=500):
    num_ingredients = len(ingredients)
    best_score = 0
    best_amounts = None

    def generate_combinations(index, amounts, remaining):
        nonlocal best_score, best_amounts

        # Base case: last ingredient gets all remaining teaspoons
        if index == num_ingredients - 1:
            amounts.append(remaining)
            score = calculate_score(amounts, ingredients, check_calories, target_calories)
            if score > best_score:
                best_score = score
                best_amounts = amounts.copy()
            amounts.pop()
            return

        # Try all possible amounts for current ingredient
        for amount in range(remaining + 1):
            amounts.append(amount)
            generate_combinations(index + 1, amounts, remaining - amount)
            amounts.pop()

    generate_combinations(0, [], total_teaspoons)
    return best_score, best_amounts


ingredients = parse_ingredients(ingredients_params)
score, amounts = find_best_cookie(ingredients)
print(f"Best score: {score}")
print(f"Amounts: {[f'{name}: {amt}' for (name, _), amt in zip(ingredients, amounts)]}")
