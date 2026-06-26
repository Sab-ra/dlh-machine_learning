# Notes

## Five card-dies vectors

You create 5 vectors by drawing 5 cards with the replacement and trhowing 3 dies.

### Generate data-set

$$X^{(1)} = {{Q \diamonds} \brack {2+1+1}} = {12 \brack 4}$$
$$X^{(2)} = {{4 \diamonds} \brack {5+2+3}} = {4 \brack 10}$$
$$X^{(3)} = {{J \hearts} \brack {6+3+1}} = {11 \brack 10}$$
$$X^{(4)} = {{10 \spades} \brack {5+6+6}} = {10 \brack 17}$$
$$X^{(5)} = {{J \clubs} \brack {4+1+1}} = {11 \brack 6}$$

### Mean vector 

$$\mu = {{\mu_{ranks}} \brack {\mu_{dies}}} = {9.6 \brack 9.4}$$

So, which rank was the closest to $\mu_{ranks}$? - $Experiment 4$

### Small sigma (Standard Deviation and Variance)

$$\sigma = \sqrt{{\sum{|{\mu-x}|}} \over n}$$

$$\sigma_{ranks} = \sqrt{{\sum{|{\mu_{ranks}-x_{ranks}}|}} \over n}$$
$$\sigma_{ranks} = \sqrt{{{(9.6 - 12)^2 + (9.6 - 4)^2 + (9.6 - 11)^2 + (9.6 - 10)^2 + (9.6 - 11)^2}} \over 5} = \sqrt{{{41.2}} \over 5} = 2.871$$

### Variance

$$\sigma^2$$

Because variance is just standard deviatition squared, well, probably you can start calculating variance, and then standard deviation out of it, by taking square root.

$$\sigma^2 = {{\sum{{\mu-x}}} \over n}$$
$$\sigma_{ranks}^2 = {{{(9.6 - 12)^2 + (9.6 - 4)^2 + (9.6 - 11)^2 + (9.6 - 10)^2 + (9.6 - 11)^2}} \over 5} = {{{41.2}} \over 5} = 8.24$$
$$\sigma_{dies}^2 = {{{(9.4 - 4)^2 + (9.4 - 10)^2 + (9.4 - 10)^2 + (9.4 - 17)^2 + (9.4 - 6)^2}} \over 5} = {{{99.2}} \over 5} = 19.84$$

then

$$\sigma_{dies} = \sqrt{19.84} = 4.454$$

### Covairance Matrix

I expect, but I am not sure:
$$Cov = \begin{bmatrix}
   8.24 & 0 \\
   0 & 19.84
\end{bmatrix}$$

Well, my not sure was correct, because this matrix above is called `diagonal case` of **covariance matrix** when huge amount of statistics _prove_ cards and dies being totally independent. And here we have only five statistics to look at. So, we assume that those **random variables** are dependent.

#### To find Covariance Matrix

You look how each trial 'moves away' from the mean (vector-wise i suppose)

Meet **Product of Differences** `POD`

$$POD = {(Rank - \mu_{Rank}) * (Die - \mu_{Die})}$$

$$POD_1 = {(12 - 9.6) * (4 - 9.4)} = 2.4 * (-5.4) = -12.96$$
$$POD_2 = -3.36$$
$$POD_3 = 0.84$$
$$POD_4 = 3.4$$
$$POD_5 = -4.76$$

Then we need an average of the product of differences

$$POD = {{\sum POD_n} \over n}$$
$$POD = -3.368$$

And then you stush that POD instead of zeros into **covariance matrix _diagonal case_** 

$$\Sigma = 

{\begin{bmatrix}
   8.24 & POD \\
   POD & 19.84
\end{bmatrix}} = 

{\begin{bmatrix}
   8.24 & -3.368 \\
   -3.368 & 19.84
\end{bmatrix}}

$$

This covariance matrix shows **negative relationship** (-3.368) That is why if we plot the statistics the 'ellips' of probability would rather tilt downward. -- correct

### Inverse of Covariance Matrix

#### Determinant $|\Sigma|$

$$|\Sigma| = (8.24 * 19.84) - (-3.368)^2 = 152.1382$$

#### Matrix of Minors

For 2x2 matrix, just swap start with end: $
\Sigma_m =
{\begin{bmatrix}
   19.84 & -3.368 \\
   -3.368 & 8.24
\end{bmatrix}}
$

#### Matrix of Cofactors {+-+-+-+} & Adjugate

$
\Sigma_{cofactors} = 
{\begin{bmatrix}
   19.84 & 3.368 \\
   3.368 & 8.24
\end{bmatrix}} =
\Sigma_{adjugate}
$

Because **matrix of cofactors** is simmetrical, the **adjugate** will be the same matrix.

#### Scalar Multiply $\Sigma_{adjugate}$ by $|\Sigma|^{-1}$ to get $\Sigma^{-1}$

$$
\Sigma^{-1} = 
{\begin{bmatrix}
   19.84 \over 152.1382 & 3.368 \over 152.1382 \\
   3.368 \over 152.1382 & 8.24 \over 152.1382
\end{bmatrix}} = 
{\begin{bmatrix}
   0.13 & 0.02 \\
   0.02 & 0.05
\end{bmatrix}}
$$
