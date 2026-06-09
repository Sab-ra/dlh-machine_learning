#!/usr/bin/env python3
"""Exponental module"""


class Exponental:
    """Will be meaningful"""

    def __init__(self, data=None, lambtha=1.):
        """Initialise through the setter"""
        self.__data = None
        self.__lambtha = None

        if data is not None:
            self.data = data
        else:
            self.lambtha = lambtha

    """getters & setters"""

    @property
    def lambtha(self):
        """get lambtha value"""
        return self.__lambtha
    
    @lambtha.setter
    def lambtha(self, value):
        """set valid value of lambtha"""
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
        if not isinstance(value, list):
            raise TypeError("data must be a list")
        if len(value) < 2:
            raise ValueError("data must contain multiple values")
        if not all(isinstance(x, (int, float)) for x in value):
            raise TypeError('data must contain only numbers')
        self.__data = value
        self.__lambtha = sum(value) / len(value)

