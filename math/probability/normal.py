#!/usr/bin/env python3
"""Normal distribution module"""


class Normal:
    """Gives mean and std dev-on for data sets"""

    def __init__(self, data=None, mean=0., stdev=1.):
        """Constructor init"""
        self.__data = None
        self.__mean = None
        self.__stdev = None

        if data is not None:
            self.data = data
        else:
            self.mean = mean
            self.stdev = stdev

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
        if not(all(isinstance(x, (int, float)) for x in value)):
            raise TypeError('data must contain only numbers')
        self.__data = value

        # calculate mean and stdev from data
        self.__mean = self.__calculate_mean(value)
        self.__stdev = self.__calculate_stdev(value)

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
    def stdev(self):
        """get standard deviation value"""
        return self.__stdev
    
    @stdev.setter
    def stdev(self, value):
        """set valid standard deviation"""
        if self.__data is not None:
            raise ValueError('cannot set stdev when data')
        if not isinstance(value, (int, float)):
            raise TypeError('stdeviation must b a number')
        if value <= 0:
            raise ValueError('stddev must be a positive value')
        self.__stdev = float(value)

    """helpers"""
    def __calculate_mean(self, data):
        "calculate mean from data"
        return sum(data) / len(data)

    def __calculate_stdev(self, data):
        """calculate stdev from data"""
        mad = []
        for i in range(len(data)):
            dev = self.__calculate_mean(data) - data[i]
            mad.append(dev ** 2)
        return (sum(mad) / (len(mad) - 1)) ** (1/2)
        