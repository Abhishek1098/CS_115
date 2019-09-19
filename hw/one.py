from cs115 import *

def factorial(i):
    #Takes p  ositive int i and returns factorial
    return reduce(multiply, range(1, i + 1))


def multiply(i, j):
    #Returns the product of two ints
    return i * j


def mean(L):
    #Takes in list returns average
    return reduce(sum, L) / len(L)


def sum(i, j):
    #Takes two ints and returns sum
    return i + j 


def divides(i):
    def div(j):
        return i % j == 0
    return div

def isPrime(n):
    #function takes in positive int n and returns whether n is prime
    return map(divides(n), range(1, n + 1)).count(True) == 2

    
