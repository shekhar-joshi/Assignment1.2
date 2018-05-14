#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 01:54:57 2018

@author: shekhar
"""

"""Create the below pattern using nested for loop in Python.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""

for i in range(0,5):            #we actually do not need the nested loop to draw this pattern
    for j in range(0,1):    #its used to enter the nested loop and the initialize it to value 1 again
        print("* "*i)
        
for i in range(5,0,-1):
    for j in range(0,1):
        print("* "*i)
    
