#!/usr/bin/env python3
"""Element-wize Add/Substract"""


def np_elementwise(mat1, mat2):
    """Function"""
    return (
        (mat1 + mat2),
        (mat1 - mat2),
        (mat1 * mat2),
        (mat1 / mat2)
    )
