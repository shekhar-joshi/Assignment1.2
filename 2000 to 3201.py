# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
l=[]
for i in range(2000,3201):
    if((i % 7 ==0) and ( i % 5 != 0 )):    
        l.append(i)
print(l)