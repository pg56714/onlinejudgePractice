def partition_equal_subset(n):
    total_sum = n * (n + 1) // 2

    if total_sum % 2 != 0:
        return "NO"

    target = total_sum // 2

    subset1 = []
    subset2 = []

    for num in range(n, 0, -1):
        if target >= num:
            subset1.append(num)
            target -= num

    subset1_set = set(subset1)
    subset2 = [num for num in range(1, n + 1) if num not in subset1_set]

    if len(subset1) > len(subset2):
        subset1, subset2 = subset2, subset1

    subset1_str = ",".join(map(str, sorted(subset1)))
    subset2_str = ",".join(map(str, sorted(subset2)))
    return f"YES,[{subset1_str}],[{subset2_str}]"


input_str = int(input())
result = partition_equal_subset(input_str)
print(result)
