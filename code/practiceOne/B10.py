a, b, c, d = map(int, input().split())


def time_difference(h1, m1, h2, m2):

    start_minutes = h1 * 60 + m1
    end_minutes = h2 * 60 + m2

    if end_minutes >= start_minutes:
        return end_minutes - start_minutes
    else:
        return 1440 - start_minutes + end_minutes


print(time_difference(a, b, c, d))
