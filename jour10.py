# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 07:38:21 2020

@author: gverquiere
"""
from copy import deepcopy
input_str = [0]
cible = 0
with open ('input10.css', 'r') as f :
    for line in f :
        input_str.append(int(line.strip()))
input_str.sort()
input_str.append(input_str[-1]+3)
print(input_str)
dist = {1:0, 2:0, 3:0}

for k in range(1, len(input_str)):
    dist[input_str[k]-input_str[k-1]]+=1
print(dist)
print(dist[3]*dist[1])
cpt = 0
possible = [[0]]

dic = {input_str[-1]:1}
for k in range(len(input_str)-2, -1, -1):
    c = 0
    for pas in [1,2,3]:
        if input_str[k] + pas in dic.keys() :
            c+= dic[input_str[k] + pas]
    dic[input_str[k]] = c
print(dic[0])

print(cpt)