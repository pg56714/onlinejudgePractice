def perform_shift_operations(input_string):
    import re

    s = "ABCDEF"

    operations = re.findall(r"\{(\d+)\}", input_string)

    for op in operations:
        # print(op)
        n = int(op) - 1
        if n < 0 or n >= len(s):
            continue

        s = s[1 : n + 1] + s[0] + s[n + 1 :]

    return s


input_str = input().strip()
print(perform_shift_operations(input_str))
