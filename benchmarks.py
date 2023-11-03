# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
           Information sciences 179.13 (2009): 2232-2248.	

 -- Purpose: Defining the benchmark function code 
              and its parameters: function Name, lowerbound, upperbound, dimensions

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy
import math


    
def F1(x):
  """ Spere Function """
  s=numpy.sum(x**2);
  return s



def getFunctionDetails(a):
  # [name, lb, ub, dim]
  param = {  0: ["F1",-100,100,30],
            }
  return param.get(a, "nothing")



