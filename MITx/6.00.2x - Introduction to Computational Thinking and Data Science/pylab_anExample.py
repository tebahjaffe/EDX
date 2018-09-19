#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 17:38:03 2018

@author: tebahsaboun
"""

# An example of retirement fund

import pylab as plt

def retire(monthly,rate,terms):
    savings=[0]
    base=[0]
    mRate=rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1+mRate)+monthly]
    return base,savings
    
def displayRetireWMonthlies(monthlies,rate,terms):
    plt.figure("retireMonth")
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly,rate,terms)
        plt.plot(xvals,yvals,label="retire: "+str(monthly))
        plt.legend(loc='upper left')
        
def displayRetireWRates(monthly,rates,terms):
    plt.figure('retireMonth')
    plt.clf()
    for rate in rates:
        xvals,yvals=retire(monthly,rate,terms)
        plt.plot(xvals,yvals,label="retire: "+str(rate))
        plt.legend(loc='upper left')
        
def displayRetireWMonthsAndRates(monthlies,rates,terms):
    plt.figure('retireBoth')
    plt.clf()
    for monthly in monthlies:
        for rate in rates:
            xvals,yvals = retire(monthly,rate,terms)
            plt.plot(xvals,yvals,label='retire: '+str(monthly)+ ':' \
                     +str(int(rate*100)))
            plt.legend(loc='upper left')
            
def displayFinal(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12,40*12)
    monthLabels = ['r','b','g','k']
    rateLabels = ['-','o','^']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals,yvals = retire(monthly,rate,terms)
            plt.plot(xvals,yvals,monthLabel+rateLabel,label='retire: ' \
                     +str(monthly)+ ':'+str(int(rate*100)))
            plt.legend(loc = 'upperleft')
            
        

monthlys = [500,600,700,800,900,1000,1100]

rates = [0.03,0.05,0.07]

#displayRetireWMonthlies(monthlys,0.05,40*12)

#displayRetireWRates(800,rates,40*12)

#displayRetireWMonthsAndRates(monthlys,rates,40*12)

displayFinal(monthlys,rates,40*12)