# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:39:21 2020

@author: gverquiere
"""
import os
from copy import deepcopy

input_str = []
with open ('input6.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))
        
group = [[]]
for line in input_str :
    if len(line) == 0 :
        group.append([])
    else :
        group[-1].append(line)


cpt = 0
for g in group:

    question = []

    for q in g[0] :
        question.append(q)

    for personne in g :
        copy_question = deepcopy(question)
        for q in copy_question :

            if not q in personne :

                question.remove(q)

    cpt+=len(question)
    
    print(cpt)
        
