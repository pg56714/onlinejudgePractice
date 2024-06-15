from itertools import permutations


def generate_permutations(n):
    str_n = str(n)
    unique_numbers = set()

    for perm in permutations(str_n):
        num_str = str(int("".join(perm)))
        if num_str != str_n:
            unique_numbers.add(int(num_str))

    result = sorted(unique_numbers, reverse=True)

    return result


input_str = input()
result = generate_permutations(input_str)
for num in result:
    print(num)
