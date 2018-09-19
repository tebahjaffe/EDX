#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:21:55 2018

@author: tebahsaboun
"""
import random

class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name
    
    def set_age(self,newage):
        self.age=newage
        
    def set_name(self,newname=""):
        self.name=newname
    
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class Cat(Animal):
    def speak(self):
        print("miaou")
    
    def __str__(self):
        return "Cat:"+str(self.name)+":"+str(self.age)

class Rabbit(Animal):
    tag=1
    
    def __init__(self,age,parent1=None,parent2=None):
        assert isinstance(parent1)==Rabbit and isinstance(parent2)==Rabbit
        Animal.__init__(self,age)
        self.parent1=parent1
        self.parent2=parent2
        Rabbit.rid=Rabbit.tag
        Rabbit.tag+=1
        
    def get_rid(self):
        return str(self.rid).zfill(3)
    
    def get_parent1(self):
        return self.parent1
    
    def get_parent2(self):
        return self.parent2
    
    def speak(self):
        print("meep")
    
    def __str__(self):
        return "Rabbit:"+str(self.name)+":"+str(self.age)  

    def __add__(self,other):
        return Rabbit(0,self,other)

class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        Animal.set_name(self,name)
        self.friends=[]
    
    def get_friends(self):
        return self.friends
    
    def add_friend(self,friend):
        if friend not in self.friends:
            self.friends.append(friend)
    
    def speak(self):
        print("hello")
    
    def age_diff(self,other):
        #alternate way : diff=self.age - other.age
        diff=self.get_age() - other.get_age()
        if diff>0:
            print(self.name," is ",str(diff)," years older than ",other.name)
        else:
            print(self.name," is ",str(-diff)," years younger than ",other.name)
            
    def __str__(self):
        return "Person:"+str(self.name)+":"+str(self.age)  

class Student(Person):
    def __init__(self,name,age,major=None):
        Person.__init__(self,name,age)
        self.major=major
        
    def change_major(self,major):
        self.major=major
    
    def speak(self):
        r=random.random()
        if r<0.25:
            print("I have homework")
        elif 0.25<=r<0.5:
            print("I need sleep")
        elif 0.5<=r<0.75:
            print("I need to eat")
        else:
            print("I am going to watch tv")
    
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
        
        