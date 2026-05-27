#!/usr/bin/env python3
"""Module that calculates the cofactor of a matrix"""


def cofactor(matrix):
    """Calculate the cofactor of a matrix"""

    minor = __import__('1-minor').minor
    minor_matrix = minor(matrix)
    n = len(minor_matrix)

    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
        if i % 2 == 0:
            for j in range(n):
                if j % 2 == 0:
                    cofactor_row.append(minor_matrix[i][j])
                else:
                    cofactor_row.append(-minor_matrix[i][j])
        else:
            for i in range(n):
                if j % 2 == 0:
                    cofactor_row.append(-minor_matrix[i][j])
                else:
                    cofactor_row.append(minor_matrix[i][j])
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix
