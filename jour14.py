# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 07:03:32 2020

@author: gverquiere
"""
input_str = []
from copy import deepcopy
with open ('input14.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))
print(input_str)
mem={}
mask =''
for line in input_str :
    if line.startswith('mask =') :
        mask = line[7:]
    else :
        t = line.split('] = ')
        value = int(t[1])
        position = int(t[0][4:])
        binary = '{0:036b}'.format(value)
        real = ''
        for k in range (len(binary)):
            if mask [k] == 'X' :
                real += binary[k]
            else :
                real += mask[k]
        value = int(real, 2)
        mem[position] = value
print(mem)

cpt = 0
for key in mem.keys():
    cpt += mem[key]
print(cpt)

mem={}
mask =''
for line in input_str :
    if line.startswith('mask =') :
        mask = line[7:]
    else :
        t = line.split('] = ')
        value = int(t[1])
        position = int(t[0][4:])
        binary = '{0:036b}'.format(position)
        real = ['']
        for k in range (len(binary)):
            copy = deepcopy(real)
            if mask [k] == 'X' :
                temp =[]
                for s in copy :
                    temp.append(s+'1')
                    temp.append(s+'0')
                real = temp
            elif  mask [k] == '0' :
                for s in range (len(real)) :
                    real[s] += binary[k]
            else :
                for s in range (len(real)) :
                    real[s] += '1'
        for position in real :
            val = int(position, 2)
            mem[position] = value
print(mem)

cpt = 0
for key in mem.keys():
    cpt += mem[key]
print(cpt)
