# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
           Information sciences 179.13 (2009): 2232-2248.	

Purpose: Defining the move Function
            for calculating the updated position

Code compatible:
 -- Python: 2.* or 3.*
"""

import random

def move(PopSize,dim,pos,vel,acc):
    for i in range(0,PopSize):
        for j in range (0,dim):
            r1=random.random()
#           r2=random.random()
            vel[i,j]=r1*vel[i,j]+acc[i,j]
            pos[i,j]=pos[i,j]+vel[i,j]
    
    return pos, vel
