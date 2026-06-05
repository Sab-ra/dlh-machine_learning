#!/usr/bin/env python3
"""Calculate derivative of polinomial"""


def poly_derivative(poly):
    """Imagine poly as array: i=power, v=coefficient"""
    if not isinstance(poly, list):
        return None
    if not all(isinstance(i, (int, float)) for i in poly):
        return None
    n = len(poly)
    if n == 0:
        return None
    if n == 1:      # constant
        return 0
    drvtv = []
    for x in range(1, n):
        drvtv.append(x * poly[x])
    return drvtv
