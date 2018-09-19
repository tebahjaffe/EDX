#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 14:42:56 2018

@author: tebahsaboun
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    for elem in L: 
        if g(f(elem))==False:
            print(g(f(elem)))
            L.remove(elem)
            print(L)

    if L==[]:
        return -1
    else:
        L.sort()
        return L[len(L)-1]


def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]

applyF_filterG(L, f, g)
print(L)

