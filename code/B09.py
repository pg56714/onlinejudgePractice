a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())


# 用遞迴解會超時
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


n = 56 * a + 24 * b + 14 * c + 6 * d
n1 = 56 * e + 24 * f + 14 * g + 6 * h

fib_n = fibonacci(n)
fib_n1 = fibonacci(n1)
print(fib_n)
print(fib_n1)
