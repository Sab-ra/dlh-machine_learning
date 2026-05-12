#!/usr/bin/env python3
"""Mirror, transpose!"""


def matrix_transpose(matrix):
"""Loop to swap raws with columns"""

    result = []

    for col in range(len(matrix[0])):
        new-row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        result.append(new_row)

    return result
