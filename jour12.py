# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 09:17:41 2020

@author: gverquiere
"""
input_str = []
cible = 0
with open ('input12.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))
        
test = ["F10",
"N3",
"F7",
"R90",
"F11"]

direction = 'E'
position = [0,0] #NORD EST
waypoint = [1, 10]

for cons in input_str :
    d = cons[0]
    nb = int(cons[1:])
    if d =='F':
        position[0] += nb* waypoint[0]
        position[1] += nb* waypoint[1]
        #d=direction
    if d=="N":
        waypoint[0]+=nb
    if d=="S":
        waypoint[0]-=nb
    if d=="E":
        waypoint[1]+=nb
    if d=="W":
        waypoint[1]-=nb
    if d=="L":
        
        cpt = nb//90
        for k in range(cpt) :
            #direction = {'E':'S', 'S':'W', 'W':'N', 'N':'E'}[direction]
            a = waypoint[0]
            b = waypoint[1]
            waypoint[0] = b
            waypoint[1] = -a
    if d=="R":
        cpt = nb//90
        for k in range(cpt) :
            #direction = {'E':'N', 'S':'E', 'W':'S', 'N':'W'}[direction]
            a = waypoint[0]
            b = waypoint[1]s
            waypoint[0] = -b
            waypoint[1] = a
    print("=====")
    print(waypoint)
    print(position)  


print(abs(position[0]) +abs(position[1]))     