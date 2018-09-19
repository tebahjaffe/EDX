#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:14:20 2018

@author: tebahsaboun
"""

class Food(object):
    def __init__(self,n,v,w):
        self.name=n
        self.value=v
        self.calories=w
        
    def getValue(self):
        return self.value
        
    def getCalories(self):
        return self.calories
    
    def getDensity(self):
        return self.getValue()/self.getCalories()
    
    def __str__(self):
        return self.name + ' : <' + str(self.getValue()) + ", " + str(self.getCalories()) + ' >'

    
def BuildMenu(names,values,calories):
    """names, values, calories lists of same length 
    names list of strings,
    values and calories lists of numbers
    return list of Foods """
    menu=[]
    for i in range(len(values)):
        menu.append(Food(names[i],values[i],calories[i]))
        
    return menu
    
def greedy(items,maxCost,keyFunction):
    """ Assumes items a list, maxCost >= 0,
    keyFunction maps elements of items to numbers"""
    
    itemsByKey = sorted(items,key=keyFunction,reverse=True)
    
    result = []
    totalValue, totalCost = 0.0, 0.0
    
    for i in range(len(itemsByKey)):
        if (totalCost + itemsByKey[i].getCalories()) <= maxCost:
            result.append(itemsByKey[i])
            totalCost += itemsByKey[i].getCalories()
            totalValue += itemsByKey[i].getValue()
    
    return (result,totalValue)

def maxVal(toConsider,avail):
    """ Assumes toConsider to be a list of items,
        avail a weight,
        returns a tuple of the totaql value of the solution 
        to a 0/1 knapsack problem and the items of that solution"""
    if toConsider==[] or avail==0:
        result=(0,())
    elif toConsider[0].getCalories()>avail:
        result=maxVal(toConsider[1:],avail)
    else:
        nextItem=toConsider[0]
        withVal,withToTake=maxVal(toConsider[1:],avail-nextItem.getCalories())
        withVal+=nextItem.getValue()
        withoutVal,withoutToTake=maxVal(toConsider[1:],avail)
        if withVal>withoutVal:
            result=(withVal,withToTake+(nextItem,))
        else:
            result=(withoutVal,withoutToTake)
    return result

def testGreedy(items,constraint,keyFunction):
    taken, val = greedy(items,constraint,keyFunction)
    print("Total value of items taken",val)
    for item in taken:
        print('  ', item)

def testmaxVal(items,constraint):
    val, listTaken = maxVal(items,constraint)
    print("Total value of items taken",val)
    for item in listTaken:
        print('  ', item)

def testGreedys(foods,maxUnits):
    print('Use greedy by value to allocate',maxUnits,' calories')
    testGreedy(foods,maxUnits,Food.getValue)
    
    print('\nUse greedy by cost to allocate',maxUnits,' calories')
    testGreedy(foods,maxUnits,lambda x: 1/Food.getCalories(x))
    
    print('\nUse greedy by density to allocate',maxUnits,' calories')
    testGreedy(foods,maxUnits,Food.getDensity)
        
        
names = ['wine','beer','pizza','burger','fries','cola','apple','donut','cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]

foods=BuildMenu(names,values,calories)
#testGreedys(foods,750)
testmaxVal(foods,750)

        
                
        
    