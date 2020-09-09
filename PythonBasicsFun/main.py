# a one line comment
# comments are ignored by Python

'''
this is 
a multi line
comment
'''

# variables
# a variable store a value
# they also have a data type 
# (what range of values can be stored)
x = 5 # "x is assigned 5" 
# the data type of x is integer
print(type(x))
x = 5.5 # floating point value (fractional)
print(type(x))
my_name = "gina" # string (sequence of characters)
print(my_name)

# operators
# * multiplication
# / floating point division
# // integer division
print(5 / 2)
print(5 // 2)
# remember PEMDAS
# also print a python operator precedence table
# ** power
print(2 ** 5)
# you can import math module
# sqrt() pow() tan()
import math # by convention, all imports should be at
# the top of the file
print(math.pow(2, 5))
