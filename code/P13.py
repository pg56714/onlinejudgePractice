def base3_to_base10(base3_str):
    int_part, dec_part = base3_str.split(".")
    int_part = sum(int(num) * (3**i) for i, num in enumerate(reversed(int_part)))

    dec_part = sum(int(num) * (3 ** (-i - 1)) for i, num in enumerate(dec_part))

    return int_part + dec_part


def round_repeats(base9_dec_part):
    # print(base9_dec_part)
    seen = {}
    for i, digit in enumerate(base9_dec_part):
        # print(i, digit, seen)
        # print(digit, seen)
        # print(seen)
        if digit in seen:
            if all(prev == digit for prev in base9_dec_part[seen[digit] : i]):
                # print("repeating", base9_dec_part[seen[digit] : i])
                # print(base9_dec_part[: seen[digit] + 1], seen[digit])
                rounded_dec = round(
                    float("0." + base9_dec_part[: seen[digit] + 1]), seen[digit]
                )
                # print(rounded_dec)
                return f"{rounded_dec:.10f}".split(".")[1].rstrip("0")
        seen[digit] = i
    return base9_dec_part


def base10_to_base9(base10_num):
    int_part = int(base10_num)
    dec_part = base10_num - int_part
    base9_int_part = ""

    while int_part > 0:
        base9_int_part = str(int_part % 9) + base9_int_part
        int_part //= 9

    if not base9_int_part:
        base9_int_part = "0"
    base9_dec_part = ""
    counter = 0

    while dec_part > 0 and counter < 12:
        dec_part *= 9
        base9_dec_part += str(int(dec_part))
        dec_part -= int(dec_part)
        counter += 1
    base9_dec_part = round_repeats(base9_dec_part)

    return f"{base9_int_part}.{base9_dec_part if base9_dec_part else '0'}"


# examples = ["210.112", "0.21001", "110222.0", "22110.1021"]
# outputs = [base10_to_base9(base3_to_base10(example)) for example in examples]
# print(outputs)

input_str = input()

print(base10_to_base9(base3_to_base10(input_str)))
