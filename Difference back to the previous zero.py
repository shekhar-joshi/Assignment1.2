#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 23:16:46 2018

@author: shekhar

Assignment 6.1

Consider a DataFrame df where there is an integer column 'X':
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
For each value, count the difference back to the previous zero (or the start of the Series,
whichever is closer).
These values should therefore be [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]. Make this a new column 'Y'.
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
l=[]
l=df["X"].tolist()
l
i = 0
r = []

for element in l:
    if element != 0:
        i += 1
    else:
        i = 0
    r.append(i)

df.insert(1,"Y",r)
df