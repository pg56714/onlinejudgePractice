def has_hump(input_string):
    numbers = [int(char) for char in input_string]

    for i in range(1, len(numbers) - 1):
        left_nums = numbers[:i]
        right_nums = numbers[i + 1 :]

        # 檢查當前數字是否比左右側數字都大
        if numbers[i] > max(left_nums) and numbers[i] > max(right_nums):
            return 1
    return 0


input_string = input()

print(has_hump(input_string))
