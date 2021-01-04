# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 07:47:54 2020

@author: gverquiere
"""
import os
from copy import deepcopy

input_str = []
with open ('input8.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))
        


for str_id in range(len(input_str)):
    lines =[]
    line =0
    acc = 0
    if input_str[str_id][0:3] == 'jmp'  :
        input_str[str_id]=input_str[str_id].replace('jmp','nop')

        while line not in lines :
            lines.append(line)
            if line == len(input_str):
                print(acc)
            elif input_str[line][0:3] == 'nop':       
                line +=1
            
            elif input_str[line][0:3] == 'acc': 
                if input_str[line][4] == '+' :
                    acc+= int(input_str[line][5:])
                elif input_str[line][4] == '-' :
                    acc-= int(input_str[line][5:])
                else : print ('Error')
                line +=1
            elif input_str[line][0:3] == 'jmp': 
                if input_str[line][4] == '+' :
                    line+= int(input_str[line][5:])
                elif input_str[line][4] == '-' :
                    line-= int(input_str[line][5:])
                else : print ('Error') 
    
        
        input_str[str_id]=input_str[str_id].replace('nop','jmp')
    elif input_str[str_id][0:3] == 'nop' :
        input_str[str_id]=input_str[str_id].replace('nop','jmp')

        while line not in lines :
            lines.append(line)
            if line == len(input_str):
                print(acc)
            
            elif input_str[line][0:3] == 'nop':       
                line +=1
            
            elif input_str[line][0:3] == 'acc': 
                if input_str[line][4] == '+' :
                    acc+= int(input_str[line][5:])
                elif input_str[line][4] == '-' :
                    acc-= int(input_str[line][5:])
                else : print ('Error')
                line +=1
            elif input_str[line][0:3] == 'jmp': 
                if input_str[line][4] == '+' :
                    line+= int(input_str[line][5:])
                elif input_str[line][4] == '-' :
                    line-= int(input_str[line][5:])
                else : print ('Error') 
        input_str[str_id]=input_str[str_id].replace('jmp','nop')

    
