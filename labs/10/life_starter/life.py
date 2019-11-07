#
# life.py - Game of Life lab
#
# Name:Abhishek Yadav
# Pledge:"I pledge my honor that I have abided by the Stevens Honor System."
#

import random
import sys


def printBoard( A ):
    """ this function prints the 2d list-of-lists
        A without spaces (using sys.stdout.write) """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )


def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width, height):
    """returns a 2d array with "height" rows and "width" cols"""
    A = []
    for row in range(height):
        A += [createOneRow(width)]    # What do you need to add a whole row here?
    return A


def diagonalize(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A


def innerCells(width, height):
    """ creates a board and then modifies it to have a
        border of 1s around the center
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            A[row][col]= 0
    for row in range(1, height-1):
        for col in range(1, width-1):
            A[row][col]= 1
    return A


def randomCells(width, height):
    A = innerCells(width, height)
    for row in range(1, height-1):
        for col in range(1, width-1):
            if random.choice([0,1]) == 0:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A


def copy(A):
    width = len(A[0])
    height = len(A)
    B = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            B[row][col] = A[row][col]
    return B


def innerReverse(A):
    B = copy(A)
    height = len(B)
    width = len(B[0])
    for row in range(1, height-1):
        for col in range(1, width-1):
            if A[row][col] == 0:
                B[row][col] = 1
            else:
                B[row][col] = 0
    return B


def next_life_generation( A ):
    """ makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays 0.
    """
    def testCell(C, row, col):
        """ takes in row, col and nested array. tests cell based on game rules"""
        width = len(C[0])
        height = len(C)

        neighbors = []
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if r >= 0 and r < height and r >= 0 and r < width:
                    if r != row or c != col:
                        neighbors = neighbors + [C[r][c]]    
        
        aliveCount = 0
        for cell in neighbors:
            if cell == 1:
                aliveCount += 1
                
        if aliveCount < 2 or aliveCount > 3:
            return 0
        elif aliveCount == 3:
            return 1
        else:
            return C[row][col]

        
    B = copy(A)
    
    height = len(B)
    width = len(B[0])
    
    for row in range(1, height-1):
        for col in range(1, width-1):
            B[row][col] = testCell(A, row, col)

    return B
    
    

