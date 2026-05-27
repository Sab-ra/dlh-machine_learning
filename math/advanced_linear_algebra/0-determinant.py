#!/usr/bin/env python3
"""Calc Determinant by Gaussan Elim"""


def determinant(matrix):
    """Preseve integers on computation"""
    # variables:
    n = len(matrix)
    A = [row[:] for row in matrix]
    det = 1
    scale = 1

    # validate matrix variable
    if not isinstance(matrix, list) or \
    not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not all(len(row) == n for row in matrix):
        if matrix == [[]]:
            return 1
        else:
            raise ValueError("matrix must be a square matrix")

    for i in range(n):
        if A[i][i] == 0:
            for k in range(i+1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    det *= -1
                    break
            else:
                return 0
        pivot = A[i][i]

        for j in range(i+1, n):
            if A[j][i] != 0:
                target = A[j][i]

                for k in range(i, n):
                    A[j][k] = pivot * A[j][k] - target * A[i][k]

                scale *= pivot

    for i in range(n):
        det *= A[i][i]
    return det // scale
