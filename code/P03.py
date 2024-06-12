def judge_trend(input_string):
    is_ascending = True
    is_descending = True

    for i in range(len(input_string) - 1):
        if input_string[i] >= input_string[i + 1]:
            is_ascending = False
        if input_string[i] <= input_string[i + 1]:
            is_descending = False

        if not is_ascending and not is_descending:
            return 3

    if is_ascending:
        return 1
    if is_descending:
        return 2

    return 3


input_string = input()

print(judge_trend(input_string))
