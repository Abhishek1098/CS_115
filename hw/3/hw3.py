'''
Created on 9/23/19
@author:   Abhishek Yadav
Pledge:    I pledge my honor to abide by the Stevens Honor Code

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

def giveChange(amount, coins):

    if amount == 0:
        return [0, []]
    if coins == [] or amount < 0:
        return [float('inf'), []]
    else:
        use = giveChange(amount - coins[0], coins)
        lose = giveChange(amount, coins[1:])
        
    use = [use[0] + 1, use[1] + [coins[0]]]
    return min(use,lose)


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]

    '''
    if dct:
        return [dct[0], wordScore(scrabbleScores, dct[0])] + wordsWithScore(dct[1:], scrabbleScores)
    return []


def wordScore(dct, word):
    '''
        Dictionary of words is dct, word is the word we want the score of
        function takes score of the first letter and calls wordScore again without the first letter
    '''
    if word:
        return letterScore(dct, word[0]) + wordScore(dct, word[1:])
    return 0


def letterScore(dct, let):
    '''
        checks if first element in dictionary is the letter and returns the score if not then returns
        a new dictionary without the first element
    '''
    if (dct[0][0] == let):
        return dct[0][1]
    return letterScore(dct[1:], let)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n == 0 or not L:
        return []
    return [L[0]] + take(n - 1, L[1:])

        

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if not L:
        return []
    if n == 0:
        return [L[0]] + drop(n, L[1:])
    return drop(n - 1, L[1:])


