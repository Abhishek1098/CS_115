'''
Created on 10/10/19
@author:   Abhishek Yadav
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 != 0

'''101010'''

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''

    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n // 2) + str(1)
    else:
        return numToBinary(n // 2) + str(0)

'''Odd base 10 number will have a 1 at the
end and an even base 10 number will have a 0.
It's because the 2^0 digit is the only place in the base 2
system that is odd'''

'''Original // 2 = new'''

'''if N is even then you can add 0 to the end and if its odd add 1'''
        

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if not s:
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])


def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    inc = 8*"0" + numToBinary(binaryToNum(s) + 1)
    return inc[-8:]



def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n >= 0:
        print(s)
        count(increment(s), n -1)

'''59 = 2012'''


def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''

    if n == 0:
        return ''
    elif n % 3 == 0:
        return numToTernary(n // 3) + str(0)
    else:
        return numToTernary(n // 3) + str(n % 3)


def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''

    if not s:
        return 0
    return ternaryToNum(s[:-1]) * 3 + int(s[-1])
        
