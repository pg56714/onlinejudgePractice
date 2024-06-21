def can_partition(nums):
    if len(nums) % 2 != 0 or len(nums) not in {2, 4, 6, 8, 10}:
        return 0

    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return 0

    target = total_sum // 2
    n = len(nums) // 2
    dp = [set() for _ in range(n + 1)]
    dp[0].add(0)

    for num in nums:
        for j in range(n, 0, -1):
            for prev in dp[j - 1]:
                if prev + num <= target:
                    dp[j].add(prev + num)

    return 1 if target in dp[n] else 0


input_str = list(map(int, input().strip().split(", ")))
print(can_partition(input_str))
