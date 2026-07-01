#!/usr/bin/env python3
"""Represent Multivariate Normal distribution"""
import numpy as np


class MultiNormal:
    """designed by sabra"""

    def __init__(self, data):
        """constructor"""

        self.data = data

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
        if len(value) < 2:
            raise ValueError(d_ver)

        self.__data = value


    @property
    def cov(self):
        """get covariance matrix data"""
        return self.__cov

    @cov.setter
    def __cov(self, data, mean):
        """calculate covariance"""
        data_centered = data - mean
        n = data.ndim[0]
        return (data_centered.T @ data_centered) / (n - 1)


    @property
    def mean(self):
        """get mean for data"""
        return self.__mean

    def __mean(self, data):
        """calculate mean of data"""
        return np.mean(data, axis=0, keepdims=True)
