# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 19:49:16 2023

@author: qaisar computers
"""

l=1
u=500
Anum=[]
for num in range (l,u+1):
    order=len(str(num))
    temp=num
    sum_dig=sum(int(digit)**order for digit in str(num))
    if num==sum_dig:
        Anum.append(num)
print("armstrong numbers b/w 1 and 500:")
print(Anum)
        