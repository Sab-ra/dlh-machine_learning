## 0-mean_cov.py

0. Mean and Covariance
Write a function `def mean_cov(X):` that calculates the mean and covariance of a data set:

- [x] X is a numpy.ndarray of shape (n, d) containing the data set:
- [x] n is the number of data points
- [x] d is the number of dimensions in each data point
- [x] If X is not a 2D numpy.ndarray, raise a TypeError with the message X must be a 2D numpy.ndarray
- [x] If n is less than 2, raise a ValueError with the message X must contain multiple data points
- [x] Returns: mean, cov:
- [x] mean is a numpy.ndarray of shape (1, d) containing the mean of the data set
- [x] cov is a numpy.ndarray of shape (d, d) containing the covariance matrix of the data set
You are not allowed to use the function numpy.cov

## 1-correlation.py

## multinormal.py

2. Initialize
Create the class MultiNormal that represents a Multivariate Normal distribution:

- [x] class constructor `def __init__(self, data):`
- [x] data is a numpy.ndarray of shape (d, n) containing the data set:
- [x] n is the number of data points
- [x] d is the number of dimensions in each data point
- [x] If data is not a 2D numpy.ndarray, raise a TypeError with the message data must be a 2D numpy.ndarray
- [x] If n is less than 2, raise a ValueError with the message data must contain multiple data points
Set the public instance variables:
- [x] mean - a numpy.ndarray of shape (d, 1) containing the mean of data
- [x] cov - a numpy.ndarray of shape (d, d) containing the covariance matrix data
You are not allowed to use the function numpy.cov

3. PDF
Update the class MultiNormal:

- [x] public instance method def pdf(self, x): that calculates the PDF at a data point:
- [x] x is a numpy.ndarray of shape (d, 1) containing the data point whose PDF should be calculated
- [x] d is the number of dimensions of the Multinomial instance
- [x] If x is not a numpy.ndarray, raise a TypeError with the message x must be a numpy.ndarray
- [x] If x is not of shape (d, 1), raise a ValueError with the message x must have the shape ({d}, 1)
- [ ] Returns the value of the PDF
You are not allowed to use the function numpy.cov
