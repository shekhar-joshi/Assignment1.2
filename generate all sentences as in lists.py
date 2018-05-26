#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 01:01:30 2018

@author: shekhar

Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
"""

subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

for i in subjects:
    for j in verbs:
        for k in objects:
            x = i +' '+ j+' ' + k
            print (x)
            