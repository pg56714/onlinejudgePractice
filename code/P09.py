def parse_input(input_str):
    parts = input_str.replace(" ", "").split(",")
    return parts[0], parts[1]


def base_n_to_decimal(number, base):
    decimal = 0
    power = 0
    for digit in reversed(number):
        decimal += int(digit) * (base**power)
        power += 1
    return decimal


def decimal_to_base_n(decimal, base):
    if decimal == 0:
        return "0"
    digits = []
    while decimal:
        digits.append(int(decimal % base))
        decimal //= base
    return "".join(str(x) for x in reversed(digits))


def add_numbers_in_different_bases(input_str):
    ternary, senary = parse_input(input_str)
    ternary_decimal = base_n_to_decimal(ternary, 3)
    senary_decimal = base_n_to_decimal(senary, 6)
    sum_decimal = ternary_decimal + senary_decimal
    result = decimal_to_base_n(sum_decimal, 5)
    return result


input_str = input()

print(add_numbers_in_different_bases(input_str))
