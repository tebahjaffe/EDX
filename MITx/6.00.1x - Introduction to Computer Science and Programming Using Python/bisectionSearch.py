#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:05:54 2018

@author: tebahsaboun
"""

def bisectionSearch_recur(L,e):
    if len(L)==0:
        return False
    elif len(L)==1:
        return L[0]==e
    else:
        half=len(L)//2
        if L[half]>e:
            return bisectionSearch_recur(L[:half],e)
        else:
            return bisectionSearch_recur(L[half:],e)



        
    
                