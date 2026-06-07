#!/usr/bin/env python3
"""Plotting a line graph with Matplotlib"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(y, color = "red")
    plt.xlim(0, 10)
    plt.savefig('line.png')
    plt.show()

if __name__ == '__main__':
    line()
