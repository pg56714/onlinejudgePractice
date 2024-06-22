def custom_sort_key(char):
    if char.islower():
        # print("lower", ord("z") - ord(char))
        # # print("z", ord("z")) # 122
        # print("char", ord(char))
        return ord("z") - ord(char)
    else:
        # print("upper", ord("Z") - ord(char) + 26)
        # print("char", ord(char))
        return ord("Z") - ord(char) + 26


def middle_character(s):
    # custom sort key
    sorted_string = "".join(sorted(s, key=custom_sort_key))
    middle_index = len(sorted_string) // 2
    return sorted_string[middle_index]


input_str = input().strip()
print(middle_character(input_str))
