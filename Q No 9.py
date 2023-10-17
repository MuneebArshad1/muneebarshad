# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:16:43 2023

@author: qaisar computers
"""

a=int(input("enter number 1"))
b=int(input("enter number 2"))
for i in range (a,b+1):
    if i==1:
        print("-")
    elif i==2 or i==3 or i==5 or i==7:
        print (i,"prime")
    elif i%2 == 0 or i%3 == 0 or i%5==0 or i%7==0:
        print ("-")
    else:
        print(i," prime")
    