from itertools import permutations


def is_divisible_by_11(num):
    num_str = str(num)
    # print(num_str)
    odd_sum = sum(int(num_str[i]) for i in range(0, len(num_str), 2))
    even_sum = sum(int(num_str[i]) for i in range(1, len(num_str), 2))
    # print(odd_sum, even_sum)
    return (odd_sum - even_sum) % 11 == 0


def count_divisible_permutations(n):
    str_n = str(n)
    all_perms = set(permutations(str_n))
    count = 0
    for perm in all_perms:
        perm_number = int("".join(perm))
        if is_divisible_by_11(perm_number):
            count += 1
    return count


input_str = input().strip()
print(count_divisible_permutations(input_str))
