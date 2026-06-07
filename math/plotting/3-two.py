#!/usr/bin/env python3
"""Compare half distruction C-14 VS Ra-226"""
import numpy as np
import matplotlib.pyplot as plt


def two():
    """Exponential Decay of 2 Radioactive Elements"""
    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))

    plt.title('Exponential Decay of Radioactive Elements')
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.xlim(0, 20000)
    plt.ylim(0, 1)
    plt.plot(x, y1, color="red", ls="--", label='C-14')
    plt.plot(x, y2, color="green", ls="-", label='Ra-226')
    plt.legend(loc='upper right')

    plt.savefig("3-two")
    plt.show()


if __name__ == '__main__':
    two()
