def calculate_total_cost(input_str):
    upper, lower = map(str.strip, input_str)
    # print(upper, lower)

    prices = {
        "upper": {"E": 500, "A": 800, "C": 200},
        "lower": {"E": 400, "A": 800, "C": 100},
    }

    def calculate_layer_cost(layer, prices):
        cost = 0
        count = {"E": 0, "A": 0, "C": 0}
        for char in layer:
            count[char] += 1
        for person_type, number in count.items():
            cost += prices[person_type] * number
        return cost

    upper_cost = calculate_layer_cost(upper, prices["upper"])
    lower_cost = calculate_layer_cost(lower, prices["lower"])

    total_cost = upper_cost + lower_cost

    total_people = len(upper) + len(lower)

    if total_people >= 20:
        total_cost *= 0.9

    return int(total_cost)


input_str = input().strip().split(",")
print(calculate_total_cost(input_str))
