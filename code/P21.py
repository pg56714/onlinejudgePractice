def can_partition(nums):
    total_sum = sum(nums)
    n = len(nums)
    half = n // 2

    if total_sum % 2 != 0:
        return 0

    target = total_sum // 2

    dp = [[False] * (target + 1) for _ in range(half + 1)]
    dp[0][0] = True

    for num in nums:
        for count in range(half, 0, -1):
            for j in range(target, num - 1, -1):
                if dp[count - 1][j - num]:
                    dp[count][j] = True

    for j in range(target + 1):
        if dp[half][j] and j * 2 == total_sum:
            return 1
    return 0


input_str = input()
nums = list(map(int, input_str.strip().split(",")))
print(can_partition(nums))
