'''
Created on _______________________
@author:   Abhishek Yadav
Pledge:    _______________________

CS115 - Lab 5
'''
import time
from cs115 import map

words = []
HITS = 10

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''

    def editDist(first, second):
        if (first, second) in data:
            return data[(first, second)]
        if first == "" or second == "":
            value = max(len(first), len(second))
        elif first[0] == second[0]:
            value = editDist(first[1:], second[1:])
        else:
            branch = 1 + editDist(first[1:], second)
            branch2 = 1 + editDist(first, second[1:])
            branch3 = 1 + editDist(first[1:], second[1:]) 
            value = min (branch, branch2, branch3)
            
        data[(first, second)] = value
        return value

    data = {}
    return editDist(first, second)


def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda w : (fastED(w, user_input), w), words)
    


def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
