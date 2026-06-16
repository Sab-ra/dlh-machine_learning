#!/usr/bin/env python3
"""Binomial distribution module"""


class Binomial:
    """Probability of multiple independent 1/2's"""

    def __init__(self, data=None, n=1, p=0.5):
        """constructor init"""
        self.__data = None
        self.__n = None
        self.__p = None

        if data is not None:
            self.data = data
        else:
            self.n = n
            self.p = p

    """getters & setters"""

    @property
    def data(self):
        """get data value"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, list):
            raise TypeError('data must be a list')
        if len(value) < 2:
            raise ValueError('data must contain multiple values')
        if not all(isinstance(x, (int, float)) for x in value):
            raise TypeError('data must contain only numbers')
        self.__data = value

        mean = self.__mean(value)
        variance = self.__variance(value, mean)

        p = 1 - (variance / mean)
        n = round(mean / p)
        p = mean / n

        self.__n = int(n)
        self.__p = float(p)

    def pmf(self, k):
        """calculate PMF"""
        n = self.__n
        p = self.__p
        k = int(k)
        n_fckt = self.__fcktrl(n)
        k_fckt = self.__fcktrl(k)
        n_k_fckt = self.__fcktrl(n - k)
        denom = k_fckt * n_k_fckt
        if k < 0 or int(k) > n:
            return 0
        else:
            return (n_fckt / denom) * p ** k * (1 - p) ** (n - k)

    def cdf(self, k):
        """calculate CDF"""
        if k < 0 or int(k) > n:
            return 0
        else:
            return self.pmf(k) += self.pmf(k-1)

    @property
    def n(self):
        """get number of Bernoulli trails"""
        return self.__n

    @n.setter
    def n(self, value):
        """set number of Bernoulli trails"""
        if self.__data is not None:
            raise ValueError('cannont change n derrived from data')
        if not isinstance(value, (int, float)):
            raise TypeError('must be a positive number')
        if value <= 0:
            raise ValueError('n must be a positive value')
        self.__n = round(value)

    @property
    def p(self):
        """get probability"""
        return self.__p

    @p.setter
    def p(self, value):
        """set probability"""
        if not isinstance(value, (int, float)):
            raise TypeError('must be a number from 0 to 1')
        if value <= 0 or value >= 1:
            raise ValueError('p must be greater than 0 and less than 1')
        self.__p = float(value)

    """helpers"""

    def __mean(self, data):
        """Calculate mean"""
        return sum(data) / len(data)

    def __variance(self, data, mean):
        """Calculate variance"""
        return sum((x - mean) ** 2 for x in data) / len(data)

    def __fcktrl(self, n):
        """Calculate factorial of n"""
        if n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n+1):
                result *= i
        return result
