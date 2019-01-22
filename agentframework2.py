# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:14:40 2019

@author: davidh
"""

# Import modules

import random


#A class for an agent that can moe in space and interact with other agents ands its environment
class Agent ():
    #behaviours of agents
    def __init__(self, environment, agents, number, startx, starty):
        
#agents within the environmnet 
        self.environment = environment
#communicating between agents
        self.agents = agents
#agent house number
        self.number = number
#start location of x and y to the pub start location (found by reading the environment)
        self._x = startx
        self._y = starty
#agent cannot start have arrived at the start
        self.arrived = False
        
        
        
#Moving the agents randomly = random_move 
#consticted to moving within the environment - cannot beyond the environmnet limits        
    def random_move (self):
               
        if random.random() <0.5:
            xrandom_move=self._x+1
            if xrandom_move<len(self.environment) and xrandom_move>0:
                self._x = xrandom_move    
        else:
            xrandom_move=self._x-1
            if xrandom_move<len(self.environment) and xrandom_move>0:
                self._x = xrandom_move
        if random.random() <0.5:
            yrandom_move=self._y+1
            if yrandom_move<len(self.environment) and yrandom_move>0:
                self._y = yrandom_move     
        else:
            yrandom_move=self._y-1
            if yrandom_move<len(self.environment) and yrandom_move>0:
                self._y = yrandom_move
  
    
#Tested a move faster option where afents would move 2 instead of 1 
#resulted in the agents getting home much quicker
#but the density map created became much harder to read and much more unclear
"""
def random_move_faster (self):
               
        if random.random() <0.5:
            xrandom_move=self._x+2
            if xrandom_move<len(self.environment) and xrandom_move>0:
                self._x = xrandom_move    
        else:
            xrandom_move=self._x-2
            if xrandom_move<len(self.environment) and xrandom_move>0:
                self._x = xrandom_move
        if random.random() <0.5:
            yrandom_move=self._y+2
            if yrandom_move<len(self.environment) and yrandom_move>0:
                self._y = yrandom_move     
        else:
            yrandom_move=self._y-2
            if yrandom_move<len(self.environment) and yrandom_move>0:
                self._y = yrandom_move  
"""