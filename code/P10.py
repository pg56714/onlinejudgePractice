def can_divide_all(input_str):
    numbers = list(map(int, input_str.split(",")))

    for num in numbers:
        # all can check if all elements in the list are True
        if all(other % num == 0 for other in numbers):
            return 1

    return 0


input_str = input()

print(can_divide_all(input_str))


# def can_divide_all(input_str):
#     numbers = list(map(int, input_str.split(',')))

#     for num in numbers:
#         can_divide = True
#         for other in numbers:
#             if other % num != 0:
#                 can_divide = False
#                 break

#         if can_divide:
#             return 1
#     return 0
