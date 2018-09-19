#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 09:41:15 2018

@author: tebahsaboun
"""
import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
##Creating a plot
#plt.figure('linear')
##Clearing the window in case we replot
#plt.clf()
##Labelling x and y axis
#plt.xlabel('sample points')
#plt.ylabel('linear function')
#plt.ylim(0,1000)
#plt.plot(mySamples,myLinear)
#plt.plot(mySamples,myQuadratic)
#plt.figure('quadratic')
#plt.clf()
#plt.ylim(0,1000)
#plt.plot(mySamples,myQuadratic)
#plt.figure('cubic')
#plt.clf
#plt.plot(mySamples,myCubic)
#plt.figure('expo')
#plt.clf()
#plt.plot(mySamples,myExponential)
#plt.figure('quadratic')
#plt.ylabel('quadratic function')
#
##Adding titles
#plt.figure('linear')
#plt.title('linear')
#plt.figure('quadratic')
#plt.title('quadratic')
#plt.figure('cubic')
#plt.title('cubic')
#plt.figure('expo')
#plt.title('exponential')

#Creating a new plot 
plt.figure('lin vs quad')
#Cleaning the plot
plt.clf()
#Plotting the function and adding a label to it
plt.plot(mySamples,myLinear,label='linear')
plt.plot(mySamples,myQuadratic,label='quadratic')
#Placing the labels (legends) on the figure
plt.legend(loc='upper left')
#Adding a title to our figure
plt.title('Linear vs Quadratic')

plt.figure("cube vs exp")
plt.clf()
plt.plot(mySamples,myCubic,label='cubic')
plt.plot(mySamples,myExponential,label='exponential')
plt.legend()
plt.title('Cubic vs Exponential')

