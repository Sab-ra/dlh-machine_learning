#!/usr/bin/env python3
"""Module calcs adjugate of matrix"""


def adjugate(matrix):
    """Uses cofactor imported"""

    cofactor = __import__('2-cofactor').cofactor

    cof_of_matrix = cofactor(matrix)

    n = len(cof_of_matrix)

    adjugate = []

    for i in range(n):
        adjugate_row = []
        for j in range(n):
            adjugate_row.append(cof_of_matrix[j][i])
        adjugate.append(adjugate_row)
    return adjugate
