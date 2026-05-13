#!/usr/bin/env python3
"""Concatenate Matrices"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Axis=0: stash, Axis=1: side_by_side"""
    mat = []
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        else:
            for row in mat1:
                mat.append(row)
            for row in mat2:
                mat.append(row)
            return mat
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        else:
            mat = list(map(lambda row: row[0] + row[1], zip(mat1, mat2)))
            return mat
