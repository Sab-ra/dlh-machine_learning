#!/usr/bin/env python3
"""Normal distribution module"""


class Normal:
    """Gives mean and std dev-on for data sets"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Constructor init"""
        self.__data = None
        self.__mean = None
        self.__stddev = None

        if data is not None:
            self.data = data
        else:
            self.mean = mean
            self.stddev = stddev

    def z_score(self, x):
        """calc z-score of a given x value"""
        return (x - self.__mean) / self.__stddev

    def x_value(self, z):
        """calc x-value from given z-score"""
        return z * self.__stddev + self.__mean

    """getters & setters"""

    @property
    def data(self):
        """get data value"""
        return self.__data

    @data.setter
    def data(self, value):
        """set valid data"""
        if not isinstance(value, list):
            raise TypeError('data must be a list')
        if len(value) < 2:
            raise ValueError('data must contain multiple values')
        if not (all(isinstance(x, (int, float)) for x in value)):
            raise TypeError('data must contain only numbers')
        self.__data = value

        # calculate mean and stddev from data
        self.__mean = self.__calculate_mean(value)
        self.__stddev = self.__calculate_stddev(value)

    @property
    def mean(self):
        """get mean value"""
        return self.__mean

    @mean.setter
    def mean(self, value):
        """set mean: data or default"""
        if self.__data is not None:
            raise ValueError('cannot set mean when data')
        self.__mean = float(value)

    @property
    def stddev(self):
        """get standard deviation value"""
        return self.__stddev

    @stddev.setter
    def stddev(self, value):
        """set valid standard deviation"""
        if self.__data is not None:
            raise ValueError('cannot set stddev when data')
        if not isinstance(value, (int, float)):
            raise TypeError('stddeviation must b a number')
        if value <= 0:
            raise ValueError('stddev must be a positive value')
        self.__stddev = float(value)

    """helpers"""

    def __sqrt(self, x):
        """calculate SQRT with Newtons method"""
        if x <= 0:
            return 0
        guess = x
        for _ in range(100):
            guess = (guess + x / guess) / 2
        return guess

    def __calculate_mean(self, data):
        "calculate mean from data"
        return sum(data) / len(data)

    def __calculate_stddev(self, data):
        """calculate stddev from data"""
        mean = self.__calculate_mean(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return self.__sqrt(variance)
