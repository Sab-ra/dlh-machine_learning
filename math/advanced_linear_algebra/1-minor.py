#!/usr/bin/env python3
"""Modul that calcs minor (not cofactor) of a matrix"""


def minor(matrix):
    """Validate matrix variable"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == []:
        raise ValueError("matrix must be a non-empty square matrix")
    
    n = len(matrix)

    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    
    minor_matrix = []

    """Base Case: 1x1 matrix has minor [[1]]"""
    if n == 1:
        minor_matrix = [[1]]
        return minor_matrix
    
    """Base Case: 2x2 matrix has minor [[d, c], [b, a]]"""
    if n == 2:
        a, b = matrix[0]
        c, d = matrix[1]
        minor_matrix = [[d, c], [b, a]]
        return minor_matrix
    
    """Recursive Step: For larger matrices, calc minor of each element"""
    determinant = __import__('0-determinant').determinant
    for i in range(n):
        minor_row = []
        for j in range(n):
            # Create submatrix by excluding row i and column j
            submatrix = [row[:j] + row[j+1:] for k, row in enumerate(matrix) if k != i]
            minor_row.append(determinant(submatrix))
        minor_matrix.append(minor_row)

    return minor_matrix
