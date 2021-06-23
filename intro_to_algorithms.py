# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 15:42:08 2021

@author: megan
"""

# Topics:
    # 1. Algorithms
    # 2. Expressing Functions (the math kind) in Python
    # 3. Optimization
    
    
# import modules
import pandas as pd # we typically use this function to read in & manipulate files
import os # We use this to set our working directory
import sqlite3 # This is the sql module we saw with Assignment 8
import csv
import numpy as np 
import math # this module gives us a variety of math functions like abs, round, etc.
import doctest # this is our testing module
from typing import List, Tuple

#--------------------------------------------------------------------

# Topic 1: Algorithms
# For the purposes of this class, an algorithm is a set of steps that 
# accomplishes a task. Each function in a program, as well as the 
# program itself, is an algorithm.

# So the functions we covered yesterday were essentially algorithms. 
# Today, we'll work with a few slightly more complex ones, pulling in 
# other concepts and modules, as needed.

# Function 1: Find and return the smallest value in the list 
list1 = [709, 821, 621, 238, 17, 222, 935, 100, 322, 446]
def minimum(list: List[float]) -> float:
    """
    Return the smallest value in list L.
    """
    smallest = list[0]
    
    for i in range(2, len(list)):
        if list[i] < smallest:
            smallest = list[i]
    return smallest

smallest = minimum(list1)
print(smallest)


# Pro tip: 
# the sorted() function returns a list that is sorted in ascending order
sorted_list = sorted(list1) 
# We can use this in algorithms where we need to find max/min values
# then we can index at [0] for the smallest, and [list length - 1] for
# the largest value

# we can also remove/insert values into our list
index = list1.index(smallest) # find the index of the smallest

list1.remove(smallest)
list1.insert(index, smallest) # put it back


# Practice Problem!

# Function 2: Find and return the largest value in the list
listx = [709, 821, 621, 238, 17, 222, 935, 100, 322, 446]

def maximum(listx: List[float]) -> float:
    maxval = listx[0]
    for i in range(len(listx)):
        if listx[i] > maxval:
            maxval = listx[i]
    return maxval 

print(maximum(listx))

#--------------------------------------------------------------------

# Topic 2: Expressing Math Equations in Python

# Our Exercise: Calculate Free Fall & the amount of time it takes for an
# object to hit the ground given all other values
# Formula: h_t = -(1/2)gt^2 + v_0*t + h_0
# our constants: h_t = 0, g = 9.81

# We start with representing our formula in python
# Function 3: Formula
def free_fall(v_0: float, h_0: float, t: float) -> float:
    """
    represents the free fall formula, given a v_0, h_0, and t
    uses the constant g = 9.81
    """
    return -(1/2)*(9.81)*(t**2) + v_0*t + h_0

print(free_fall(5, 17.9, 5.5))


# Function 4: Calculate the first derivative
def first_deriv(v_0: float, h_0: float, t: float) -> float:
    """
    represents the first derivative of the free fall formula
    """
    return v_0 - 9.81*t


# Function 5: Maximize function to find the h when the function is at its peak
# Formula: h_t = -(1/2)gt^2 + v_0*t + h_0
# our constants: h_t = 0, g = 9.81
def max_h(v_0: float, h_0: float) -> float:
    """
    calculates the t when h_t = 0
    """
    # we know we can find the first derivative and set it = to zero to see where
    # the function reaches its maximum
    
    # 0 = v_0 - 9.81*t
    # 9.81t = v_0
    # t = v_0/9.81
    
    t = v_0/9.81
    
    # now that we know our t, we can use our first function to find the h_t 
    # at the maximum point
    return free_fall(v_0, h_0, t)

    
# Practice Problems!

# Function 6: Represent the following formula in code
# Formula: h = (1/2)a*t^2 - v*t
def formula(a: float, t: float, v: float) -> float:
    return (1/2) * (a * (t**2)) - (v * t)

# Function 7: Calculate the first derivative
def derivative(a: float, t: float, v: float) -> float:
    return v + a*t

# Function 8: Minimize the function
def minimium(a: float, v: float) -> float:
    t = v/a
    return formula(a, t, v)

#--------------------------------------------------------------------

# Topic 3: Optimizing

# For this class, solving an optimization problem involves finding a parameter 
# input that achieves the maximum or minimum value of a particular objective function

# Exercise 5 & 6 from Assignment 5    
# Exercise 4, 5, and 6 from the Midterm
# Question 1 & 2 from Assignment 7
