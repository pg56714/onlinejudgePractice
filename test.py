def knapsack(values, weights, W):
    n = len(values)

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            # print(f"i: {i}, w: {w}")
            print(i, weights[i - 1], w)
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
                print(dp[i][w])
            else:
                dp[i][w] = dp[i - 1][w]
                print(dp[i][w])

    return dp[n][W]


values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

max_value = knapsack(values, weights, W)
print("Max value: ", max_value)
