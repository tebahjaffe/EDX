#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:25:53 2018

@author: tebahsaboun
"""
import pylab as plt

mySamples=[]
myLinear=[]
myQuadratic=[]
myCubic=[]
myExponential=[]

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    

#first trial 
plt.plot(mySamples,myLinear)
plt.plot(mySamples,myQuadratic)
plt.plot(mySamples,myCubic)
plt.plot(mySamples,myExponential)

#second trial 
plt.figure("linear")
plt.xlabel("sample points")
plt.ylabel("linear function")
plt.clf()
plt.plot(mySamples,myLinear)
plt.figure("quadratic")
plt.clf()
plt.plot(mySamples,myQuadratic)
plt.figure("cubic")
plt.clf()
plt.plot(mySamples,myCubic)
plt.figure("exponential")
plt.clf()
plt.plot(mySamples,myExponential)
plt.figure("lin vs quad")
plt.clf()
plt.plot(mySamples,myLinear,'b-',label="linear",linewidth = 2.0)
plt.plot(mySamples,myQuadratic,'r',label="quadratic",linewidth = 3.0)
plt.legend()
plt.title("linerar versus quadratic")
