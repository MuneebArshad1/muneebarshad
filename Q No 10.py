# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:14:25 2023

@author: qaisar computers
"""
b=0
c=0
d=0
while True:
    a=int(input("enter number"))
    l=input("enter c to continue or done to finish")
    if a==0:
        b=b+1
    if a<0:
        c=c+1
    if a>0:
        d=d+1
    if l == "c":
        continue
    if l == "done":
        break
    
print (b,"zeros",c,"-ve numbers",d,"+ve numbers")
    