#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:26:39 2018

@author: tebahsaboun
"""

import datetime

class Person(object):
    def __init__(self,name):
        """ Create a person called name """
        self.name=name
        self.birthday=None
        self.lastName=name.split(' ')[-1]
        
    def getlastName(self):
        return self.lastName
    
    def getBirthday(self):
        return self.birthday
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def setBirthday(self,month,day,year):
        self.birthday=datetime.date(year,month,day)
    
    def getAge(self):
        if self.birthday==None:
            raise ValueError
        return ((datetime.date.today() - self.birthday).days)/360
    
    def __lt__(self,other):
        if self.lastName==other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
class MITPerson(Person):
    nextIdNum=0     #next ID Number to assign
    def __init__(self,name):
        Person.__init__(self,name)      # initializes Person attributes
        self.idNum=MITPerson.nextIdNum  # MITPerson attribute : unique ID
        MITPerson.nextIdNum += 1
    
    def getIdNum(self):
        return self.idNum
    
    # Sorting MIT People using their ID number, not their name !
    def __lt__(self,other):
        return self.idNum < other.idNum
    
    def speak(self,utterance):
        return (self.getlastName()+" says:"+ utterance)
    

p1=Person('Mark Zuckerberg')
p1.setBirthday(5,14,1984)
p2=Person('Drew Houston')
p2.setBirthday(3,4,1983)
p3=Person('Bill Gates')
p3.setBirthday(10,28,1955)
p4=Person('Andrew Gates')
p5=Person('Steve Wozniak')

personList=[p1,p2,p3,p4,p5]

for person in personList:
    print(person)
    
personList.sort()

for person in personList:
    print(person)