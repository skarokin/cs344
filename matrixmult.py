def two_matrix_mult(A, B):
    a11, a12, a21, a22 = A[0][0], A[0][1], A[1][0], A[1][1]
    b11, b12, b21, b22 = B[0][0], B[0][1], B[1][0], B[1][1]
    c11 = a11*b11 + a12*b21
    c12 = a11*b12 + a12*b22
    c21 = a21*b11 + a22*b21
    c22 = a21*b12 + a22*b22
    return [[c11, c12], [c21, c22]]

def recursive_matrix_mult(A, B):
    # base case: 2x2 matrix; consider this as constant time
    if len(A) == 2:
        return two_matrix_mult(A, B)

    # split the matrices into quarters
    n = len(A) // 2
    A11, A12, A21, A22 = A[:n, :n], A[:n, n:], A[n:, :n], A[n:, n:]
    B11, B12, B21, B22 = B[:n, :n], B[:n, n:], B[n:, :n], B[n:, n:]

    # recursively calculate each quarter
    c11 = recursive_matrix_mult(A11, B11) + recursive_matrix_mult(A12, B21)
    c12 = recursive_matrix_mult(A11, B12) + recursive_matrix_mult(A12, B22)
    c21 = recursive_matrix_mult(A21, B11) + recursive_matrix_mult(A22, B21)
    c22 = recursive_matrix_mult(A21, B12) + recursive_matrix_mult(A22, B22)

    return [[c11, c12], [c21, c22]]

def loop_mult(A, B):
    C = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(A)):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[1,2, 3, 4, 5, 6, 7, 8],[1,2, 3, 4, 5, 6, 7, 8]]
B = [[10, 11, 12, 13, 14, 15, 16, 17],[10, 11, 12, 13, 14, 15, 16, 17]]
print(recursive_matrix_mult(A, B))
print(loop_mult(A, B))
