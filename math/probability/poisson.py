#!/usr/bin/env python3
"""Module contains poisson distribution class"""


class Poisson:
    """Poisson Hacked"""
    def __init__(self, data=None, lambtha=1.):
        """data <- list, lambtha <- number occurances"""

        if data is None:
            if not isinstance(lambtha, (int, float)):
                raise TypeError('lambtha must be a number')
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """calculate P(X=k) with known lambtha"""
        lambtha = self.lambtha
        probka = 0
        if k < 0:
            return probka
        else:
            k = int(k)
            e = 2.7182818285
            nom = e ** (-1 * lambtha) * lambtha ** k
            denom = self.__factorial(k)
            probka = nom / denom
            return probka
        
    def cdf(self, k):
        probleska = 0
        if k < 0:
            return probleska
        else:
            k = int(k)
            pmfs = []
            for i in range(k+1):
                pmfs.append(self.pmf(i))
            probleska = sum(pmfs)
            return probleska

    def __factorial(self, n):
        """Calculate factorial"""
        if n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n+1):
                result *= i
        return result
