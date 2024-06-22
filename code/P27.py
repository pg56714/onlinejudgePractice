def longest_substring_divisible_by_ten(s):
    def char_to_number(c):
        # print(ord(c.upper()))
        # print(ord("Z") - ord("A"))
        # print(ord(c.upper()) - ord("A") + 1)
        return ord(c.upper()) - ord("A") + 1

    n = len(s)
    prefix_sum = 0
    first_occurrence = {0: -1}
    max_length = 0

    for i in range(n):
        prefix_sum += char_to_number(s[i])
        remainder = prefix_sum % 10

        if remainder in first_occurrence:
            max_length = max(max_length, i - first_occurrence[remainder])
        else:
            first_occurrence[remainder] = i

        # print(
        #     i,  # index
        #     prefix_sum,  # prefix sum
        #     remainder,  # remainder
        #     first_occurrence,  # first occurrence
        #     first_occurrence[remainder],  # first occurrence of remainder
        #     i - first_occurrence[remainder],  # current length
        #     max_length,  # max length
        # )

    return max_length


input_str = input().strip()
print(longest_substring_divisible_by_ten(input_str))
