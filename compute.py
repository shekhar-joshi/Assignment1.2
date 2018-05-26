#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:46:20 2018

@author: shekhar

Write a function to compute 5/0 and use try/except to catch the exceptions.
"""
def compute():
    return 5/0
    
try:
    compute()
except ZeroDivisionError:
    print( "division by zero!!!!!!! " )
finally:
    print("Cleaning")
    