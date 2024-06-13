def is_palindrome(s):
    return s == s[::-1]


def count_unique_letters(s):
    return len(set(s))


def longest_special_palindrome(s):
    n = len(s)
    max_length = 0

    for length in range(n, 2, -1):
        for start in range(n - length + 1):
            substr = s[start : start + length]
            if is_palindrome(substr) and count_unique_letters(substr) >= 3:
                max_length = length
                return max_length

    return max_length


input_string = input()

print(longest_special_palindrome(input_string))
