def compress_string(input_string):
    result = []
    current_char = input_string[0]
    count = 0

    for char in input_string:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1

    result.append(current_char + str(count))

    return "".join(result)


input_string = input()

print(compress_string(input_string))
