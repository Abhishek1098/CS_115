#I pledge my honor wthat I have abided by the Stevens Honor System
#Abhishek Yadav

from cs115 import *
import math

def inverse(i):
    # returns inverse of a variable, i
    return 1/i


def e(i):
    # takes a positive int in and returns the approximates
    # the mathematical value e using a Taylor expansion

    list = map(math.factorial, range(1, i+1))
    return 1 + sum( map(inverse, list) )


def error(i): 
    #Finds error between our approximation and pythons approximation
    return abs(math.e - e(i))

