def swap_letters(s):
    n = len(s)
    swapped = list(s)

    if n % 2 == 0:
        for i in range(0, n, 2):
            swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
    else:
        for i in range(n - 1, 0, -2):
            swapped[i], swapped[i - 1] = swapped[i - 1], swapped[i]

    return "".join(swapped)


input_str = input().strip()
print(swap_letters(input_str))
