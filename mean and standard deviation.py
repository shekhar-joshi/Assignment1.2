#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 20:04:53 2018

@author: shekhar

You survey households in your area to find the average rent they are paying. Find the
standard deviation from the following data:

$1550, $1700, $900, $850, $1000, $950.

"""

import pandas as pd
import numpy as np
import statistics
l=['$1550', '$1700', '$900', '$850','$1000','$950']
m=[int(s.replace('$','')) for s in l ]

print("average rent they are paying is :",statistics.mean(m))
print("standard deviation of the data :",statistics.stdev(m))
