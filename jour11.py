# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 07:55:01 2020

@author: gverquiere
"""
import os
from copy import deepcopy

input_str = []
with open ('input11.css', 'r') as f :
    for line in f :
        input_str.append([])
        for letter in str(line.strip()) :
            input_str[-1].append(letter)
        #input_str.append(str(line.strip()))
change = True
while change :
    change = False
    copy_input = deepcopy(input_str)
    for i in range (len(copy_input)):
        for j in range (len (copy_input[i])):
            cpt = 0
            for k in [-1,0,1] :
                for l in [-1,0 ,1] :
                    if k!= 0 or l!= 0:
                        cont = True
                        ii = i
                        jj = j
                        while cont  :
                            cont = False
                            
                            ii +=k
                            jj +=l
                            if ((ii) >= 0) and ((ii) < len(copy_input)) :
                                if ((jj) >= 0) and ((jj) < len(copy_input[i])) :
                                    cont = True
                                    if (copy_input[ii][jj] in [ '#','L' ]):
                                        cont = False
                                        if (copy_input[ii][jj] in ['#']):
                                            cpt +=1
            if (copy_input[i][j] =="L") and (cpt ==0):
                input_str[i][j] ="#"
                change = True
            if (copy_input[i][j] =="#") and (cpt >=5):
                input_str[i][j] ="L"
                change = True
    cpt = 0          
    copy_input = deepcopy(input_str)
    for i in range (len(copy_input)):
        for j in range (len (copy_input[i])):
            if (copy_input[i][j] =="#"):
                cpt +=1
    print (cpt)    