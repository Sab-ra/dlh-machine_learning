#!/usr/bin/env python3
def matrix_shape(matrix):  
    result = []
    while True:
        try:
            result.append(len(matrix))
            matrix = matrix[0]
        except TypeError:
            break
    return result
            