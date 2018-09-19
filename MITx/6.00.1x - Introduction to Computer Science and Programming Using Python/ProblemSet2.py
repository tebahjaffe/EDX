#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 15:52:23 2018

@author: tebahsaboun
"""

balance=999999
annualInterestRate=0.18

lowestBound=balance/12
upperBound=(balance*(1+annualInterestRate/12)**12)/12
bn=0
bnmin1=balance
epsilon=0.01
try_=(lowestBound+upperBound)/2
for i in range(0,12):
        bn=(1+annualInterestRate/12)*(bnmin1-try_)
        bnmin1=bn
while abs(bn)>epsilon:
    bn=0
    bnmin1=balance
    for i in range(0,12):
        bn=(1+annualInterestRate/12)*(bnmin1-try_)
        bnmin1=bn
    print(bn)
    if bn>0:
        lowestBound=try_
    elif bn<0:
        upperBound=try_
    try_=(lowestBound+upperBound)/2
    print(try_)
print(round(try_,2))