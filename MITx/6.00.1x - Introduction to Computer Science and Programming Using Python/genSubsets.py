#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:23:28 2018

@author: tebahsaboun
"""

def genSubsets(L):
    if len(L)==0:
        return [[]]
    smaller=genSubsets(L[:-1])
    extra=L[-1:]
    new=[]
    for small in smaller:
        new.append(small+extra)
    return smaller+new


foo=genSubsets([1,3,5,7,9])