def process_number(n):
    results = [n]
    while n != 1:
        if n % 2 == 0:
            if n >= 4:
                n //= 4
            else:
                n //= 2
        else:
            n = n * 5 + 1
        results.append(n)
    return "->".join(map(str, results))


input_str = int(input())
print(process_number(input_str))
