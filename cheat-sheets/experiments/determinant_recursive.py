#!/usr/bin/env python3
def find_determinant_r(mtx):
    n = len(mtx)
    det = 0

    # Base case 1 x 1
    if n == 1:
        det = mtx[0][0]
        return det

    # Base case 2 x 2
    if n == 2:
        det = mtx[0][0] * mtx[1][1] - mtx[0][1] * mtx[1][0]
        return det

    # Matrices 3+ x 3+
    for j in range(n):
        # Build minor remove row 0 and col j
        minor = []
        for row in mtx[1:]:
            minor.append(row[:j] + row[j+1:])

        sign = (-1) ** j
        det += sign * mtx[0][j] * find_determinant_r(minor)

    return det