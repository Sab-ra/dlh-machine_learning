#!/usr/bin/env python3
"""Modul that calcs minor of a matrix"""


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
    
    """Base Case: 1x1 matrix has minor [[1]]"""
    if n == 1:
        return [[1]]
    
    """Recursive Step: Minor of n x n is built from minors of (n-1) x (n-1)"""
    minor_matrix = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            # Build the (n-1)x(n-1) submatrix by excluding row i and column j
            submatrix = [row[:j] + row[j+1:] for k, row in enumerate(matrix) if k != i]
            minor_row.append(minor(submatrix))  # Recursive call on the submatrix
            minor_matrix.append(minor_row)
    return minor_matrix
