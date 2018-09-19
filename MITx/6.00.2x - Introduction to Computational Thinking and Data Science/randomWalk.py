#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 13:16:25 2018

@author: tebahsaboun
"""
import random

class Drunk(object):
    def __init__(self,name = None):
        self.name = name
    
    def __str__(self):
        return 'This drunk is named ' + self.name
    
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1),(0,-1),(1,0),(-1,0)]
        return random.choice(stepChoices)
    
class ColdDrunk(Drunk):
    def takeStep(self):
        # biased walk
        stepChoices = [(0.0,0.9),(0.0,-1.1),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)

#################################################################
class Location(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def move(self, deltaX, deltaY):
        """ deltaX and deltaY are floats """
        return Location(self.x+deltaX,self.y+deltaY)
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    def distFrom(self,other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
    
##################################################################
class Field(object):
    def __init__(self):
        self.drunks = {}
    
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate')
        else:
            self.drunks[drunk]=loc
    
    def getLoc(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        else:
            return self.drunks[drunk]
    
    def moveDrunk(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # use move method of Location to get to new location
        self.drunks[drunk]=currentLocation.move(xDist,yDist)
        
##################################################################
class styleIterator(object):
    def __init__(self,styles):
        self.index = 0
        self.styles = styles 
    
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result 
       
##################################################################
        
def walk(field,drunk,numSteps):
    """ Assumes numSteps an int >=0 
        Moves drunk numSteps times: returns the distance between
        the final location and the location at the start of the 
        walk """
    start = field.getLoc(drunk)
    for s in range(numSteps):
        field.moveDrunk(drunk)
    return start.distFrom(field.getLoc(drunk))

def simWalks(numSteps, numTrials, dClass):
    """ Assumes numSteps an int >=0, numTrials an int > 0,
        dClass a subclass of Drunk
        Simulates numTrials walks of numSteps steps each.
        Returns a list of final distances for each trial """
    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer,origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of ', numSteps, ' steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances

def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-','b--','g-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of ',dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
    pylab.title('Mean distance from origin (' + str(numTrials) + 'trials )')
    pylab.xlabel('Number of steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')
    
    
def drunkTest(walkLengths,numTrials, dClass):
    """ Assumes walkLengths a sequence of ints >= 0
        numTrials an int > 0 
        dClass a subclass of Drunk
        For each number of steps in walkLengths,
        run simWalks with numTrials walks and print results """
        
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of ', numSteps, ' steps')
        print('Mean = ', round(sum(distances)/len(distances), 4))
        print('Max = ', max(distances),' Min = ', min(distances))

#random.seed(0)
#drunkTest((10,100,1000,10000),100, UsualDrunk)
#drunkTest((0,1),100, UsualDrunk)
numSteps = (10, 100, 1000, 10000)
simAll((UsualDrunk,ColdDrunk), numSteps, 100)





        



        