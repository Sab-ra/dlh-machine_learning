#!/usr/bin/env python3
"""Module for Horses"""


def mat_mul(mat1, mat2):
    """Matrices multiplication"""
    if len(mat1) != len(mat2[0]):
        return None
    else:
        new_matrix = []
        for row in range(len(mat1)):
            new_row = []
            for col in range(len(mat2[0])):
                value = 0
                for x in range(len(mat2)):
                    value += mat1[row][x] * mat2[x][col]
                new_row.append(value)
            new_matrix.append(new_row)
        return new_matrix
