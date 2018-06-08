#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 20:37:03 2018

@author: shekhar

Find the variance for the following set of data representing trees in California (heights in
feet):
3, 21, 98, 203, 17, 9

"""
import numpy as np
import pandas as pd
import statistics

l = [3, 21, 98, 203, 17, 9]
v=statistics.variance(l)
print("variance of the given data is :",v)


