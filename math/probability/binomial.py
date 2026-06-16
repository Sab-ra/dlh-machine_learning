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
        #if not all(isinstance(x, (int, float)) for x in value):
        #    raise TypeError('data must contain only numbers')
        self.__data = value
        
        # calculations from data
        self.__n = self.__calculate_n(value)
        self.__p = self.__calculate_p(value)

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

    def __calculate_mean(self, data):
        """calculate mean from data"""
        return sum(data) / len(data)
    
    def __calculate_variance(self, data):
        """calculate variance from mean and data"""
        mean = self.__calculate__mean(data)
        return sum((x - mean) ** 2 for x in data) / len(data)
    
    def __calculate_n(self, mean, variance):
        """calculate Bernolli trails from mean and variance"""
        return round(mean * (1 - mean) / variance)

    def __calculate_p(self, mean, n):
        """calculate probability from mean and n"""
        return mean / n
    