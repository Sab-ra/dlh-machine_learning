#!/usr/bin/env python3
"""Module calculates mtx inverse"""


def inverse(matrix):
    """Based on Determ and Adjugate"""

    det_calc = __import__('0-determinant').determinant

    determinant = det_calc(matrix)
    if determinant == 0:
        return None
    else:
        adj_calc = __import__('3-adjugate').adjugate

        adjugate = adj_calc(matrix)
        n = len(adjugate)

        mtx_inverse = []
        for i in range(n):
            row_mtx_inv = []
            for j in range(n):
                row_mtx_inv.append(adjugate[i][j] / determinant)
            mtx_inverse.append(row_mtx_inv)

        return mtx_inverse
