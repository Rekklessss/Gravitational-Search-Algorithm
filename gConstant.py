# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
           Information sciences 179.13 (2009): 2232-2248.	
           
Purpose: Defining the gConstant Function
            for calculating the Gravitational Constant

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy

def gConstant(l,iters):
    alfa = 20
    G0 = 100
    Gimd = numpy.exp(-alfa*float(l)/iters)
    G = G0*Gimd
    return G
