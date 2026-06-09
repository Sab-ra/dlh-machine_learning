#!/usr/bin/env python3
"""Exponental module"""


class Exponential:
    """Will be meaningful"""

    def __init__(self, data=None, lambtha=1.):
        """Initialise through the setter"""
        self.__data = None
        self.__lambtha = None

        if data is not None:
            self.data = data
        else:
            self.lambtha = lambtha

    def pdf(self, x):
        """calculate probability density at a point"""
        lmbth = self.lambtha
        density = 0
        if x < 0:
            return density
        else:
            e = 2.7182818285
            density = lmbth / e ** (lmbth * x)
            return density

    def cdf(self, x):
        """calculate CDF for given time period"""
        lmbth = self.lambtha
        acculexos = 0
        if x < 0:
            return acculexos
        else:
            e = 2.7182818285
            acculexos = 1 - (1 / (e ** (lmbth * x)))
            return acculexos

    """getters & setters"""

    @property
    def lambtha(self):
        """get lambtha value"""
        return self.__lambtha

    @lambtha.setter
    def lambtha(self, value):
        """set valid value of lambtha"""
        if self.__data is not None:
            raise ValueError("cannot set lambtha when data provided")
        if not isinstance(value, (int, float)):
            raise TypeError("lambtha must be a number")
        if value <= 0:
            raise ValueError("lambtha must be a positive value")
        self.__lambtha = float(value)

    @property
    def data(self):
        """get data value"""
        return self.__data

    @data.setter
    def data(self, value):
        """set data, calc Exponential from it"""
        if not isinstance(value, list):
            raise TypeError("data must be a list")
        if len(value) < 2:
            raise ValueError("data must contain multiple values")
        if not all(isinstance(x, (int, float)) for x in value):
            raise TypeError('data must contain only numbers')
        self.__data = value
        self.__lambtha = len(value) / sum(value)
