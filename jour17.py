# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 08:07:55 2020

@author: gverquiere
"""
from copy import deepcopy
input_str = []
nb_simul =6
dim =8
with open ('input17.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))

data_map =[[[['.' for k in range (2*nb_simul +dim)] for k in range (2*nb_simul+dim)]for k in range (nb_simul*2+1)]for k in range (nb_simul*2+1)]

for i in range(nb_simul, nb_simul+dim) :
    for j in range(nb_simul, nb_simul+dim) : 
        data_map[nb_simul][nb_simul][i][j] = input_str[i-nb_simul][j-nb_simul]

for simul in range(nb_simul) :
    copy_data = deepcopy(data_map)
    for l in range(len(copy_data)) :
        for i in range(len(copy_data[l])) :
            for j in range(len(copy_data[l][i])):
                for k in range(len(copy_data[l][i][j])):
                    #On considère le point l, i, j, k
                    cpt_active = 0
                    for l_ in [-1, 0, 1] :
                        for i_ in [-1, 0, 1] :
                            for j_ in [-1, 0, 1] :
                                for k_ in [-1, 0, 1] :
                                    if (l_ != 0) or (i_ != 0) or (j_ != 0) or (k_ != 0) :
                                        #On vérifie que le point est défini
                                        if (l+l_ >=0) and (l+l_ < len(copy_data)) :
                                            if (i+i_ >=0) and (i+i_ < len(copy_data[l])) :
                                                if (j+j_ >=0) and (j+j_ < len(copy_data[l][i])) :
                                                    if (k+k_ >=0) and (k+k_ < len(copy_data[l][i][j])) :
                                                        if copy_data[l+l_][i+i_][j+j_][k+k_] == '#' :
                                                            cpt_active +=1
                    if copy_data[l][i][j][k] == '#' :
                        if (cpt_active <2) or (cpt_active >3) :
                            data_map[l][i][j][k] = '.'
                    else :
                        if (cpt_active ==3) :
                            data_map[l][i][j][k] = '#'

cpt = 0
for l in range(len(data_map)):
    for i in range(len(data_map[l])) :
        for j in range(len(data_map[l][i])):
            for k in range(len(data_map[l][i][j])):   
                if data_map[l][i][j][k] == '#' :
                    cpt+=1
print(cpt)
                                             
                    
                    
                    