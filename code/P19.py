def can_sell_all_apples(a, b):
    for x in range(max(a, b) + 1):
        y = a - 2 * x
        # print(x, y)
        if y >= 0 and x + 2 * y == b:
            return "YES"
    return "NO"


a, b = map(int, input().split())
print(can_sell_all_apples(a, b))
