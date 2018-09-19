#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 14:21:49 2018

@author: tebahsaboun
"""

import random

class Drunk(object):
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return 'This drunk is named ' + self.name
    
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
        return random.choices(stepChoices)
    
class ColdDrunk(Drunk):
    def takeStep(self):
        # biased walk
        stepChoices = [(0.0,0.9),(0.0,-1.1),(1.0,0.0),(-1.0,0.0)]
        return random.choices(stepChoices)
        