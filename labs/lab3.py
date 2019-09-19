#Created on 9/19/19
#@author:   Abhishek Yadav
#Pledge:    I Pledge my honor to abide by the Stevens Honor Code

#CS115 - Lab 3

from cs115 import *

def change(amount, coins):

    if amount == 0:
        return 0

    if amount < 0 or not coins:
        return float("inf")

    use = change(amount-coins[0], coins) + 1
    lose = change(amount,coins[1:])
    
    return min(use, lose)




