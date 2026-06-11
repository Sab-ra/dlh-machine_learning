#!/usr/bin/env python3
"""Binomial distribution module"""


class Binomial:
    """This would be special"""

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
        
        # calculations from data
        self.__p = self.__calculate__p(value)
        self.__n = self.__calculate__n(value)

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
            raise ValueError('must be a positive value')
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
        if value < 0 or value > 1:
            raise ValueError('must be greater than 0 and less than 1')
        self.__p = float(value)

    """helpers"""

    def __calculate__n(self, data):
        """calculate Bernolli trails from data"""
        return sum(data) / len(data)

    def __calculate__p(self, data):
        """calculate probability from data"""
        n = self.__calculate__n(data)
        return sum(data) / (n * len(data))
