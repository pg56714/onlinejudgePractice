def max_depth_of_nested_braces(input_str):
    current_depth = 0
    max_depth = 0

    for char in input_str:
        if char == "{":
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == "}":
            current_depth -= 1
            if current_depth < 0:
                return -1

    if current_depth != 0:
        return -1

    return max_depth


input_str = input()

print(max_depth_of_nested_braces(input_str))
