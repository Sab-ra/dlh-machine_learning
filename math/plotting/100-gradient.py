#!/usr/bin/env python3
"""Gradient Mountain Top"""
import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """Yellow close to Sun, you are the Sun"""
    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

    plt.title('Mountain Elevation')
    plt.scatter(x, y, c=z, cmap='viridis')
    plt.xlabel('x coordinate (m)')
    plt.ylabel('y coordinate (m)')
    plt.colorbar(label='elevation (m)')

    plt.savefig('100-gradient')
    plt.show()


if __name__ == '__main__':
    gradient()
