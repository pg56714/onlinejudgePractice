def read_matrix():
    dimensions = input().split()
    rows = int(dimensions[0])
    columns = int(dimensions[1])
    # print(rows, columns)
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    # print(matrix)
    # print("----")
    return matrix


def matrix_multiply(A, B):
    m, n = len(A), len(A[0])
    p, q = len(B), len(B[0])
    # print(m, n, p, q)
    if n != p:
        raise ValueError("no match for matrix multiplication")

    # result = [[0 for _ in range(q)] for _ in range(m)]
    result = [[0] * q for _ in range(m)]
    # print(result)

    for i in range(m):
        for j in range(q):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result


def format_output(matrix):
    output = "["
    # [1,2],[3,4]...
    output += ",".join(["[" + ",".join(map(str, row)) + "]" for row in matrix])
    output += "]"
    return output


A = read_matrix()
B = read_matrix()
# print(A)
# print(B)
result = matrix_multiply(A, B)
# print(result)
print(format_output(result))


# import numpy as np


# def read_matrix():
#     dimensions = input().split()
#     rows = int(dimensions[0])
#     columns = int(dimensions[1])
#     matrix = []
#     for _ in range(rows):
#         row = list(map(int, input().split()))
#         matrix.append(row)
#     return np.array(matrix)


# def matrix_multiply(A, B):
#     if A.shape[1] != B.shape[0]:
#         raise ValueError("no match for matrix multiplication")
#     return np.dot(A, B) # dot is the dot product of two arrays


# def format_output(matrix):
#     output = (
#         "[" + ",".join(["[" + ",".join(map(str, row)) + "]" for row in matrix]) + "]"
#     )
#     return output


# A = read_matrix()
# B = read_matrix()

# result = matrix_multiply(A, B)

# print(format_output(result))
