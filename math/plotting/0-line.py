#!/usr/bin/env python3
"""Plotting a line graph with Matplotlib"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """Make a red line graph of y = x^3 for x from 0 to 10."""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(y, color="red")
    plt.xlim(0, 10)
    plt.savefig('0-line.png')
    plt.show()


if __name__ == '__main__':
    line()
