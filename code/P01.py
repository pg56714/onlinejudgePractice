def find_most_frequent_char(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    most_frequent_char = ""
    max_count = 0

    for char, count in char_count.items():
        if count > max_count:
            max_count = count
            most_frequent_char = char

    return most_frequent_char


input_string = input()

print(find_most_frequent_char(input_string))
