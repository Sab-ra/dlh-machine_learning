#!/usr/bin/env python3
"""Normal way to find determinant of matrix n*n"""


def determinant(mtx):
    n = len(mtx)
    A = [row[:] for row in mtx]         # copy of mtx
    det = 1
    scale = 1

    for i in range(n):
        # find pivot
        if A[i][i] == 0:
            for k in range(i+1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    det *= -1
                    break
            else:
                return 0
            
        pivot = A[i][i]

        for j in range(i+1, n):
            if A[j][i] != 0:
                target = A[j][i]

                # integer elimination no fractions
                for k in range(i, n):
                    A[j][k] = pivot * A[j][k] - target * A[i][k]
                
                scale *= pivot      # track scaling

    # multiply diagonal
    for i in range(n):
        det *= A[i][i]

    return det // scale
    