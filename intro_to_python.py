# -*- coding: utf-8 -*-
"""
Intro to Python
Created on Thu Apr 29 16:29:14 2021

@author: megan
"""

# Topics:
    # 1. Data Types
    # 2. Operations
    # 3. Functions


# Topic 1: Data Types ----------------------------------------------
# 1. Numeric: these include Integers, Floating Point (Double-precision numbers), and Complex
    # The distinction between integers and floating points: . is needed to define a float

x = 3
type(x)

# note: integers have unlimited range (** means raised to the power of)
B = 6**1000 + 5**50
B


# 2. Boolean: this uses the reserved keywords 'True' and 'False'
x = True
type(x)
x = bool(1)
x = bool(0)
x


# 3. Strings: Delimited using single or double quotes but not combos of the 2
x = 'abc'
x
type(x)

x = 'abc123'
x
type(x)

x = '123'
x
type(x)

x = '123abc'
x

x = "123abc"
x


# Slicing strings: obtaining substrings within strings

# Slicing uses: [], where 0 is the first index and n-1 is the last
# Most common are:
    # s[i] returns character in position i
    # s[:i] returns characters from 0 to i-1
    # s[i:] returns characters from i to n-1

#       01234567890123456789012345 25 total characters
text = "I'll have 2 eggs and toast"
text[0]
text[:3]
text[4:]
text[5:8]
text[-21] # this returns n-i; since n = 25 and i = 21, this returns s[5]
text[5]


# 4. Lists: This data type holds other data
    # A list is a collection of 'objects' -- integers, floats, strings, other lists, etc
    # Lists are constructed using braces[] and values are separated using commas
    # Like with strings, lists may be sliced

x = []
type(x)
x
x = [1,2,3,4]
type(x)

# 5. Tuples: The same as lists but they are 'immutable';
# That is, they can not be changed once created
# A few notes:
    # Elements cannot be removed, added, or changed
    # Tuples are created using parentheses () or tuple() versus brackets []
    # Like lists, tuples can be sliced
    # A list can be converted to a tuple using tuple(list name)
    
ex1 = (1,2,3,4,5,6,7,8,9,10)
type(ex1)
ex1

# note: if a tuple is comprised of a single element, then a comma must be included
ex2 = (2,)
type(ex2)

# note: a list can be converted into a tuple using tuple()
ex3 = [1,2,3,4,5,6,7,8,9,10]
type(ex3)

x = tuple([ex3])
type(x)


# 6. Dictionaries: These are composed of 'keys' (strings, integers, tuples)
# and 'values' (definitions.)
# A few notes:
    # Dictionaries are used to pass 'options' into other functions
    # Keys can be strings, integers, or tuples
    # Values can contain any data type and are accessed by using keys
    
dict_1 = {'price': 225, 'beds': [2,3], 1: 'rental', (2,): 'tuple'}
type(dict_1)
dict_1['price']
dict_1['beds']
dict_1[1]
dict_1[(2,)]

# Key-value pairs can be added to an existing dictionary 
dict_1['name'] = 'Frank'
dict_1[2] = '4'
dict[1]

# Changes to existing key-value pairs may also be made
# Watch out..

dict_1['beds'] = 4
dict_1 

# Key-value pairs can be dleted using the keyword 'del'

del dict_1['name']
dict_1 

#--------------------------------------------------------------------

# Topic 2: Operations

# Addition is just the "+" symbol
print(4 + 13)

# Subtraction is just "-"
print(20 - 10)

# Division usually outputs floats
print(5/3)

# Multiplication is "*"
print(5 * 5)

# Exponentiation: We raise a number to a power using "**"
print(5 ** 2)

#--------------------------------------------------------------------

# Topic 3: Functions

# A function is a block of code that only runs when you call it.
# It accepts inputs called "parameters" and returns outputs

# We use functions to organize our "actions" in code, especially 
# actions that need to be repeated frequently, or actions that 
# can be separated to simplify other functions

# A function is defined as follows:

def function_name(input_parameters: type) -> type: 
    """
    This is your docstring. Here, you discuss what your function is,
    what it does, and what it should return. 
    
    In our class, we use the doctest testing modules, so your 
    examples go here too. 
    
    >>> function_name(sample_input)
    sample_output
    
    """
    return_type = 0
    return return_type



# Example of a function that actually works
def add_three(x: int) -> int:
    """ Returns the input + 3
    >>> add_three(1)
    4
    >>> add_three(2)
    5
    >>> add_three(3)
    6
    """
    return x + 3

# Examples of Function Calls in print statements
print(add_three(8))
print(add_three(27))




