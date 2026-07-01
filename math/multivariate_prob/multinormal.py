#!/usr/bin/env python3
"""Represent Multivariate Normal distribution"""
import numpy as np


class MultiNormal:
    """designed by sabra"""

    def __init__(self, data):
        """constructor"""

        self.data = data
        self.__mean = np.mean(data, axis=1, keepdims=True)
        d, n = data.shape
        data_centered = data - self.mean
        self.__cov = (data_centered @ data_centered.T) / (n - 1)
        self.__mn_dimentions = d

    def pdf(self, x):
        """calculate PDF at datapoint"""

        # error messages
        x_ter = f'x must be a numpy.ndarray'
        x_ver = f'x must have the shape ({self.__mn_dimentions}, 1)'

        if not isinstance(x, np.ndarray):
            raise TypeError(x_ter)
        if x.shape != (self.__mn_dimentions, 1):
            raise ValueError(x_ver)
        return 

    @property
    def data(self):
        """get data value"""
        return self.__data

    @data.setter
    def data(self, value):
        """data validation"""

        # error messages
        d_ter = f'data must be a 2D numpy.ndarray'
        d_ver = f'data must contain multiple data points'

        if not isinstance(value, np.ndarray) or value.ndim != 2:
            raise TypeError(d_ter)
        _, n = value.shape
        if n < 2:
            raise ValueError(d_ver)

        self.__data = value

    @property
    def cov(self):
        """get covariance matrix data"""
        return self.__cov

    @property
    def mean(self):
        """get mean for data"""
        return self.__mean
