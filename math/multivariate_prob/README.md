## 0-mean_cov.py

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
- [ ] mean - a numpy.ndarray of shape (d, 1) containing the mean of data
- [ ] cov - a numpy.ndarray of shape (d, d) containing the covariance matrix data
You are not allowed to use the function numpy.cov