# -*- coding: utf-8 -*-
"""
Intro to Modules
Created on Thu Apr 29 16:29:34 2021

@author: megan
"""

# Topics:
    # 1. Modules
    # 2. Loops
    # 3. Testing
    # 4. Arrays and Matrices (at the bottom)


# Topic 1: Modules
# In python, a "module" is a file that contains some pre-set functions,
# variables, and classes. Python has some modules built in that give us
# additional functionality

# Some examples we've used in the course:
import pandas as pd # we typically use this function to read in & manipulate files
import os # We use this to set our working directory
import sqlite3 # This is the sql module we saw with Assignment 8
import csv
import numpy as np
import math # this module gives us a variety of math functions like abs, round, etc.
import doctest # this is our testing module

# We can also write our own modules, as we've seen with a lot of our
# assignments


#--------------------------------------------------------------------

# Topic 2: Loops (also continuing with Topic 1 - this is where we
# build our module)

from numpy import array


# Function Definitions
# We are going to write a few functions, to go through the module
# design process, and work through the loop process

# Function 1: Just adding a value to another value
# We don't need a loop here - it's just a basic operation
def add(x: int, y: int) -> int:
    """ Returns the two inputs added together (x + y)
    >>> add(2, 2)
    4
    >>> add(3, 9)
    12
    >>> add(7, 20)
    27
    """
    return x + y

print(add(2, 2))

# Function 2: Adding a value to every element of an array
# When you want to access every element of an array, you need a
# single for loop
array1 = np.array([[10, 4, 6, 8, 12, 15, 14, 16, 13, 7, 10, 8, 6, 2, 8]])

def add_array(x: int, array1):
    """
    Returns the array with x added to every element
    >>> add_array(2, array1)
    array([[12,  6,  8, 10, 14, 17, 16, 18, 15,  9, 12, 10,  8,  4, 10]])
    >>> add_array(24, array1)
    array([[34, 28, 30, 32, 36, 39, 38, 40, 37, 31, 34, 32, 30, 26, 32]])
    >>> add_array(0, array1)
    array([[10,  4,  6,  8, 12, 15, 14, 16, 13,  7, 10,  8,  6,  2,  8]])
    """

    for i in range(len(array1)):
        # array1[i] = array1[i] + x
        # alternately, since we've written an add function,
        # we can do it like this
        array1[i] = add(array1[i], x)
    return array1

print(add_array(3, array1))



# Function 3: Adding a value to every element of a 2D array
# When you want to access every element of a 2D array, we typically
# use a nested for loop/double for loop
array2 = np.array([[10, 4, 6, 8, 12, 15, 14, 16, 13, 7, 10, 8, 6, 2, 8],
                   [100, 35, 59, 79, 98, 100, 89, 57, 63, 91, 99, 77, 85, 63, 71]])


def add_2d_array(x: int, array2):
    """
    Returns a 2D array with x added to every element

    """
    for i in range(len(array2)):
        for j in range(len(array2[i])):
            array2[i][j] = array2[i][j] + x
    return array2

print(add_2d_array(3, array2))



#--------------------------------------------------------------------

# Some Practice Exercises:

# Function 4: Summing up all the values in the array
array1 = array([10, 4, 6, 8, 12, 15, 14, 16, 13, 7, 10, 8, 6, 2, 8])

# Solution:
def add_array1(array) -> int:
    x = 0
    for i in range(len(array)):
        x += array[i]
    return x

add_array1(array1)



# Looping through and adding elements
arr = [1, 2, 3, 4, 5];
sum = 0;

# Solution:
#Loop through the array to calculate sum of elements
for i in range(0, len(arr)):
   sum = sum + arr[i];

print("Sum of all the elements of an array: " + str(sum));


# Function 5: Summing up all the values in a 2D array
array2 = np.array([[10, 4, 6, 8, 12, 15, 14, 16, 13, 7, 10, 8, 6, 2, 8],
                   [100, 35, 59, 79, 98, 100, 89, 57, 63, 91, 99, 77, 85, 63, 71]])

# Solution:
def add_array2(x):
    x1 = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            x1 += x[i][j]
    return x1

add_array2(array2)


# However, our arrays won't always be 2 dimensions, and it doesn't
# make sense to just nest another loop for every row, as that
# would get quite complicated
# Alternatively, we can do something like this:
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for row in a:
    for elem in row:
        s += elem
print(s)



# Function 6:
array3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
array4 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])


def add_array_elem(array3, array4):
    """
    Adds together the elements of 2 arrays

    """
    result = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(len(array3)):
        result[i] = array3[i] + array4[i]
    return result

add_array_elem(array3, array4)


#--------------------------------------------------------------------

# Topic 3: Testing
# This uses the doctest module we discussed in class
# it calls to all of the docstring examples, checking to see if the
# output matches the desired result

if __name__ == "__main__":
    import doctest
    doctest.testmod()



#--------------------------------------------------------------------

# Topic 4: Matrices and Arrays

# Matrices are 2 dimensional and arrays can be 1, 2, 3, etc. dimensional
    # Mathematical operations on arrays are performed element-by-element
    # Mathematical operations on matrices following the 'rules' of linear algebra
    # Arrays can be treated as matrices using either 'asmatrix' or 'mat'

# As some/many Python functions are not inculded with the base installation
# we need to import them from the 'module' in which they reside

from numpy import array
from numpy import matrix

# from numpy import *  Note: This imports everything, but may conflict
# If another imported module has functions with the same names

# Suppose x is instead a column vector. It can be coded
# as a matrix or a 2 dimensional array (using nested listing)
x = matrix([[2], [4], [6], [8]])
x = array([[2], [4], [6], [8]])

# Arrays
# Arrays are initialized from lists (or tuples) using 'array'

# First, a one-dimensional array
x = [0, 1, 2.0, 3, 4, 5.1]
y = array(x)
y
type(y)

# Next, a two dimensional array from a nested list
z = array([[0, 2, 4, 6], [8, 10, 12, 14]])
z
z.shape
z = array([[1,2], [3,4], [5,6]])

z
z.shape


# A three dimensional array from nested lists
z = array([[[1,2,1], [3,4,1]], [[5,6,1], [7,8,1.0]]])
z
z.shape

# Arrays can contain a variety of the data types we previously discussed
# 'float64' or 'double' are the most common data types
# if the array has only integers, then the data type will be 'int32',
# which is similar to 'int' seen previously
# If the array contains a mix of integers and floats.

# Now, suppose an array exists and we want to access some of its elements
# there are 4 methods for doing this:
    # 1. Scalar selection
    # 2. Slicing
    # 3. Numerical Indexing
    # 4. Logcal or Boolean indexing

# We'll consider 1 and 2. Remember: selection is 0-based
# 1. Scalar selection
# Example: The one dimensional case

#             0  1  2  3
x = np.array([1, 2, 3, 4])
x[0]
x[4]
x[3]


# Example: Two dimensional case
#              0          1          2
x = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#           0  1  2    0  1  2    0  1  2

x[0,0]
x[0,1]
x[0,2]
x[1,0]
x[1,1]
# etc.

# 2. Array Slicing
# Arrays are sliced using [: , : , etc.]
    # The slice notation is a:b:s. select the sth element in between a and b-1
    # Remember: like with lists and array selection, slicing is 0-based

    # : is the same as 0:n:1 where n is the length of the array
    # a: and a:n are the same as a:n:1
    # :b is the same as 0:b:1
    # ::c is the same as 0:n:c

#          0  1  2  3  4  5  6  7  8  9
x = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

len(x)
x[0:]
x[:10]
x[::1]
x[0:10:1] # slice every element from the first (0) to the end (10-1)
x[:]
x[0:10:2] # slice elements 0, 2, 4, etc. to the end (10-1)

# note that we need not be concerned about how many elements
# i.e., the length of the list

x[0:10:2]
x[0::2]
x[2:10:3]
x[2::3]

# With 2 dimensional arrays, the first dimension identifies the row (or rows) to slice
# and the second dimension identifies the column (or columns) to slice
# The syntax is x[a:b, c:d]

# Example: Two dimensional case
#              0          1          2
x = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#           0  1  2    0  1  2    0  1  2

x
x[0:2,1]
x[1,0:2]
x[1:3,1:3]

# Matrices work the same way as arrays, except they're fixed at
# 2 dimensions.
