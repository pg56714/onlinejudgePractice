def count_special_substrings(s):
    unique_substrings = set()

    for start in range(len(s)):
        for end in range(start + 4, len(s) + 1):
            substring = s[start:end]
            if substring[0] == substring[-1] and substring[0].isupper():
                unique_substrings.add(substring)

    return len(unique_substrings)


input_string = input()

print(count_special_substrings(input_string))
