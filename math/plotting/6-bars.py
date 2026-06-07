#!/usr/bin/env python3
"""Fruit Charge Explored"""
import numpy as np
import matplotlib.pyplot as plt

def bars():
    """People and Bananas"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4,3))
    plt.figure(figsize=(6.4, 4.8))

    plt.title('Number of Fruit per Person')
    plt.ylabel('Quantity of Fruit')
    plt.ylim(0, 80)
    plt.yticks(range(0, 90, 10))

    people = ['Farrah', 'Fred', 'Felicia']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
    fruit_names = ['apples', 'bananas', 'oranges', 'peaches']
    x = np.arange(len(people))
    width = 0.5

    bottom = np.zeros(3)
    for i in range(4):
        plt.bar(x, fruit[i], width, label=fruit_names[i], bottom=bottom, color=colors[i])
        bottom += fruit[i]

    plt.xticks(x, people)
    plt.legend()

    plt.savefig('6-bars')
    plt.show()


if __name__ == '__main__':
    bars()