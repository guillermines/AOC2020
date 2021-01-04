# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 08:25:08 2020

@author: gverquiere
"""
from copy import deepcopy
input_str=[]
with open ('input18.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))


def resolution_math(s):
    inst = s.split(' ')
    cpt = int(inst[0])
    for k in range(1,len(inst),2) :
        if inst[k]=="*":
            cpt *= int(inst[k+1])
        elif inst[k]=="+":
            cpt += int(inst[k+1])
        else : 
            print("Erreur")
    return (cpt)

def resolution_math_v2(s):
    inst = s.split(' ')
    while '+' in inst :
        pos = inst.index('+')
        inst[pos]=int(inst[pos-1]) + int(inst[pos+1])
        inst.pop(pos+1)
        inst.pop(pos-1)
    cpt = int(inst[0])
    for k in range(1,len(inst),2) :
        if inst[k]=="*":
            cpt *= int(inst[k+1])
        elif inst[k]=="+":
            cpt += int(inst[k+1])
        else : 
            print("Erreur")
    return (cpt)

def resolution_parenthese (string, start, stop):
    st_str = ""
    end_str =""
    if start >0 :
        st_str = string[0:start]
    if stop < len(string)-1:
        end_str= string[stop+1 :]
    middle = str(resolution_math_v2(string[start+1 : stop]))
    return (st_str + middle + end_str)

def resolve_line (line):
    print(line)
    while '(' in line :
        start = 0 
        for k  in range(len(line)) :
            if line[k] =='(':
                start = k
        stop = start + line[start:].find(')')
        line = resolution_parenthese(line, start, stop)
        
    return resolution_math_v2(line)
answer = 0
for line in input_str:
    answer += resolve_line(line)
print(answer)
        


        