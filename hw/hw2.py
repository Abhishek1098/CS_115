
#Created on 9/18/19
#@author:   Abhishek Yadav
#Pledge:    I Pledge my honor to abide by the Stevens Honor Code

#CS115 - Hw 2

import sys
from cs115 import map, reduce, filter
from itertools import compress 

sys.setrecursionlimit(10000)

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

#method takes a letter and finds the value from local database
def letterScore(letter, scoreList):
    element = scoreList[0]
    if letter == element[0]:
        return element[1]
    else:
        return letterScore(letter, scoreList[1:])


#method takes lowercase string and sums the value of each
def wordScore(S, scoreList):
    if S:
        return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)
    else:
        return 0

    
#checks Dictionary if words can be created from list of letters
def scoreList(Rack):
    def check(S, temp_rack):
        if not S:
            return True
        elif S[0] in temp_rack:
            temp_rack.remove(S[0])
            return check(S[1:], temp_rack)
        return False

    runCheck = lambda S : check(S, Rack[:])
    foundIndexes = (list(compress(range(len(map(runCheck, Dictionary))), map(runCheck, Dictionary))))

    output = lambda i: [Dictionary[i], wordScore(Dictionary[i], scrabbleScores)]
    return map(output, foundIndexes) if foundIndexes else ["",0]


#Finds the best word
def bestWord(Rack):
    return greatestTuple(scoreList(Rack))

    
#Finds the greatest set
def greatestTuple(L):
    if L:
        if isinstance(L[0],list):
            firstTuple = L[0]
            if len(L) == 1:
                return firstTuple
            else:
                nextTuple = greatestTuple(L[1:])
                if nextTuple[1] > firstTuple[1]:
                    return nextTuple
                else:
                    return firstTuple
        else:
            return L
    else:
        return []

