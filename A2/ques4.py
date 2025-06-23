def stationary_distribution(p, q, r, N):
    zero_index = -1
    for idx in range(N):
        if q[idx] == 0:
            zero_index = idx
    distribution = [0] * (N + 1)

    if zero_index == 0:
        total_sum = 0
        prod = 1
        for i in range(N):
            total_sum += prod
            prod *= (p[i] / q[i])
        total_sum += prod
        distribution[0] = 1 / total_sum
        factor = distribution[0]
        for i in range(N):
            distribution[i] = factor
            factor *= (p[i] / q[i])
        print(distribution)
        return distribution
    else:
        total_sum = 0
        prod = 1
        for i in range(zero_index, N):
            total_sum += prod
            prod *= (p[i] / q[i])
        total_sum += prod
        distribution[zero_index] = 1 / total_sum
        factor = distribution[zero_index]
        for i in range(zero_index, N):
            distribution[i] = factor
            factor *= (p[i] / q[i])
        print(distribution)
        return distribution


def expected_time(p, q, r, N, a, b):
    matrix = []
    for i in range(N + 1):
        matrix.append([0] * (N + 1))

    for i in range(N + 1):
        for shift in [-1, 0, 1]:
            if i < b:
                if shift == 0:
                    matrix[i][i] = 1 - r[i]
                elif shift == -1 and i + shift >= 0:
                    matrix[i][i + shift] = -q[i]
                elif shift == 1 and i + shift <= N:
                    matrix[i][i + shift] = -p[i]

    inv_matrix = inverse_gaussian(matrix)
    ones_vector = [1 for _ in range(N)]
    result_vector = multiply(inv_matrix, ones_vector)
    return result_vector[a]


def multiply(A, B):
    rows = len(A)
    cols = len(B)
    result = [[0] for _ in range(rows)]

    for i in range(rows):
        for k in range(len(A[0])):
            result[i][0] += A[i][k] * B[k]
    return result


def inverse_gaussian(A):
    size = len(A)
    identity = [[int(i == j) for j in range(size)] for i in range(size)]
    a_copy = [row[:] for row in A]

    for col in range(size):
        for row in range(size):
            if a_copy[row][col] != 0:
                divisor = a_copy[row][col]
                for k in range(size):
                    a_copy[row][k] /= divisor
                    identity[row][k] /= divisor
                for other_row in range(size):
                    if other_row != row and a_copy[other_row][col] != 0:
                        factor = a_copy[other_row][col]
                        for k in range(size):
                            a_copy[other_row][k] -= factor * a_copy[row][k]
                            identity[other_row][k] -= factor * identity[row][k]
                break
    return identity