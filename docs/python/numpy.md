---
title: Numpy
parent: Python notes
layout: default
nav_order: 6
---

# Numpy

Fast multidimensional array object and tools.

```python
import numpy as np
```

## Create array

```python
a = np.array([1, 2, 3])       # 1 dimensional array of values 1., 2., 3.
```

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
"""
array([[1, 2, 3],
       [4, 5, 6]])
"""
```

To create a 1 dimensional array of zeros

```python
a = np.zeros(10) # 10 elements of zeros
a = np.ones(10) # 10 elements of ones
```

To create an array of 9 elements with values from 3 to 19, equally spaced.

```python
a = linspace(3, 19, 9)
```

To reshape an array

```python
a = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
a.shape = (3,4) # turns it into a 2 dimensional array of 3 x 4 elements
"""
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
"""
```

To create an array of random values

```python
np.random.seed(0) # seed the random number generator
a = np.random.randint(10, size=6) # exclusive max value of 10
a = np.random.randint(0, 10, size=6) # inclusive min of 0, exclusive max value of 10
# eg: array([5, 3, 4, 8, 2, 4])
a = np.random.randint(0,10, size=(4,4)) # create a 2 dimensional array 4 x 4 elements
```

## Array properties

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
a.ndim          # number of dimensions
a.itemsize      # number of bytes in the array
a.dtype         # data type in the array
a.size          # size of the array (number of elements)
a.shape         # length in each dimension, eg (2,3)
```

## Functions to query the array

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

# returns single value results
a.max()         # maximum element value
a.min()         # minimum element value
a.sum()         # sum total of all elements
np.median(a)    # statistical median
np.prod(a)      # product (multiplication) of each element
np.argmax(a)    # index value of maximum
np.argmin(a)    # index value of minimum

# returns arrays of same size+shape with results performed on each element
np.sqrt(a)      # square root of each element
np.std(a)       # standard deviation of each element
np.sin(a)       # sine of each element
np.sort(a)      # sort the array

# evaluate each element
a < 3           # where is each element < 3
"""
array([[ True,  True, False],
       [False, False, False]])
"""
a[a < 3]        # return the array where each element is < 3
"""
array([1, 2])
"""
```

## Matrix calculations

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[3, 1, 4], [1, 5, 9]])
c = a+b         # matrix addition, eg:      [[ 4, 3, 7], [ 5,10,15]]
d = a-b         # matrix subtraction, eg:   [[-2, 1,-1], [ 3, 0,-3]]
e = a*b         # matrix multiplication, eg [[ 3, 2,12], [ 4,25,54]]
f = a/b         # matrix division, eg       [[0.3333, 2., 0.75], [4., 1., 0.6667.]]
g = a+10        # add 10 to each element
h = a*10        # multiply each element by 10
```

## Dot product based calculations

Mathematically, a dot product is the sum of multiplying the matching elements of two arrays (most commonly vectors).

Using our arrays a and b below, this would be achieved by:

* 1*3 + 2*2 + 4*6 + 5*1

There are several ways to calulate the dot product with numpy

```python
a = np.array([[1, 2], [4, 5]])
b = np.array([[3, 2], [6, 1]])

dot = np.sum(a*b)           # = 100
dot = np.dot(a,b)           # [[15, 4], [42, 13]]
dot = a.dot(b)              # [[15, 4], [42, 13]]
dot = b.dot(a)              # [[11,16], [10, 17]]
```

## Array indexing, slicing

```python
primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]

primes[2]           # = 3
primes[2:5]         # = [3, 5, 7]
primes[::-1]        # = reverses the array
primes[::2]         # = every 2nd element
```

## Image manipulation

It's quite seemless to convert back and forth between PIL images and Numpy arrays

```python
im = Image.open("/path/to/a/photo.jpg")
a = np.array(im)
print(a.shape) # (600, 800, 4)   .... (rows, columns, colour channels)
b = a[::-1] # reverses the rows in the image
Image.fromarray(b).show()
b = a[60:540, 80:720]   # create a 640x480 cut away from the centre of the photo
Image.fromarray(b).show()
```

## Transpose

```python
a = np.array([[1, 2, 3], [4, 5, 6]]).T    # The .T will swap rows and columns
"""
array([[1, 4],
       [2, 5],
       [3, 6]])
"""
```


