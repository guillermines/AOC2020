# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:53:11 2020

@author: gverquiere
"""
from copy import deepcopy
input_str = []
depart = 0
with open ('input24.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))
        
print(input_str)
#On considere une map qui garde la même colonne quand on va dans la direction NW
black_tile=[]
def get_position(s) :
    position = [0,0]
    k = 0
    while k < len(s):
        if s[k] =='w' :
            position[0] -= 1
            k+=1
        elif s[k] =='e':
            position[0] += 1
            k+=1
        elif s[k] =='n':
            position[1] += 1
            k+=1
            if s[k] =='e' :
                position[0]+=1
            k+=1
        else :
            position[1]-=1
            k+=1
            if s[k] =='w':
                position[0]-=1
            k+=1
    return (position)

def check_position (pos):
    for k in range(len(black_tile)) :
        if black_tile[k][0]== position[0]:
            if black_tile[k][1]== position[1]:
                black_tile.pop(k)
                return True
    black_tile.append(deepcopy(pos))
    return False

for s in input_str :
    position = get_position(s)
    check_position(position)
print (len(black_tile))


def apply_day(black_tile):
    result = []
    #First rule 
    for tile in black_tile :
        cpt = 0
        for voisin in [
                [0, 1],
                [1,1],
                [-1, 0],
                [1, 0],
                [-1, -1],
                [0, -1]
                ]:
            voisin_tile =[tile[k]+ voisin[k] for k in range(2)]
            if voisin_tile in black_tile :
                cpt +=1
        if (cpt in [1, 2]) :
            result.append(deepcopy(tile))
    #Second rule
    for tile in black_tile :
        #On regarde les 6 voisins
        for voisin in [
                [0, 1],
                [1,1],
                [-1, 0],
                [1, 0],
                [-1, -1],
                [0, -1]
                ]:
            voisin_tile =[tile[k]+ voisin[k] for k in range(2)]
            #On verifie que la tuile est blanche
            if not voisin_tile in black_tile :
                cpt = 0
                for v in [
                        [0, 1],
                        [1,1],
                        [-1, 0],
                        [1, 0],
                        [-1, -1],
                        [0, -1]
                        ]:                
                    is_black_tile =[voisin_tile[k]+ v[k] for k in range(2)]
                    if is_black_tile in black_tile :
                        cpt +=1
                if cpt == 2 :
                    result.append(deepcopy(voisin_tile))
    return result

def remove_copy(l):
    to_remove = []
    for k in range(len(l)-1, -1, -1):
        to_check = deepcopy(l[k])
        if to_check in l[:k]:
            to_remove.append(k)
    for k in to_remove :
        l.pop(k)
    return l

for day in range(100) :
    black_tile=apply_day(black_tile)
    remove_copy(black_tile)
    print("Day {}: {}".format(day+1, len(black_tile)))
    
    
                        

        
