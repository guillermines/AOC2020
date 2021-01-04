# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 09:14:45 2020

@author: gverquiere
"""

from copy import deepcopy
input_str=[]
with open ('input20.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))

tiles_description ={}
new = True
id_tile = 0
ti =[]
for line in input_str:
    
    if new :
        id_tile = int(line[5:-1])
        new = False
    elif line =="":
        new = True
        tiles_description[id_tile] = deepcopy(ti)
        ti =[]
    else :
        ti.append(line)
   


from copy import deepcopy
tiles ={}
for key  in tiles_description.keys() :
    i = key
    tile = tiles_description[key]
    data =[
        tile[0], #up
        "".join([tile[k][len(tile[k])-1] for k in range(len(tile))]), #right
        "".join([tile[len(tile)-1][k] for k in range(len(tile)-1, -1, -1)]), #down
        "".join([tile[k][0] for k in range(len(tile)-1, -1, -1)]), #left
        ]
    tiles[i] = deepcopy(data)

answer = 1
voisine={}
#on commence par poser une tuile au hasard
for key in tiles.keys():
    temp =[]
    tile_0 = tiles[key]
    #On cherche les tuiles qui vont au dessus
    cpt = 0
    for kk in range(4):
        to_match =[ tile_0[kk], "".join([tile_0[kk][k] for k in range(len(tile_0[kk])-1, -1,-1 )])]
        #print(to_match)
        for tile in tiles.keys():
            if tile != key :
                for cote in tiles[tile] :
                    if cote in to_match:
                        cpt +=1
                        temp.append(tile)
    voisine[key]=deepcopy(temp)
    if cpt ==2 :
        print(key)
        answer*= key
    #print(cpt)
print(answer)

def rotate(tile) :
    tt = deepcopy(tile)
    for k in range(len(tile)): #ligne
        for i in range(len(tile[k])):
            if( len(tile) - k )< len(tt[i]) :
                
                tt[i] =tt[i][:len(tile)- 1 - k] + tile[k][i] +tt[i][len(tile) - k :]
            else :
                tt[i] =tt[i][:len(tile)- 1 - k] + tile[k][i]
    return (tt)
def flip(tile) :
    tt =[]
    for k in range(len(tile) -1, -1, -1) :
        tt.append(deepcopy(tile[k]))
    return tt

#On fait maintenant la carte

#Initialisation premiere ligne
carte = [[2161, 2657]]
cont = True
while cont :
    liste_voisin = voisine[carte[0][-1]]
    for voisin in liste_voisin :
        if len(voisine[voisin]) ==3 :
            if voisin not in carte[0]:
                carte[0].append(voisin)
        if len(voisine[voisin]) ==2 :
            if voisin not in carte[0]:
                cont = False
                carte[0].append(voisin)
print(carte)
cont = True

#Creation de la carte
while cont :
    #new line
    carte.append([])
    
    #On parcourt la liste précédente
    for k in range(len(carte[-2])) :

        #On récupère les voisins
        liste_voisin = voisine[carte[-2][k]]
        possible = []
        for element in liste_voisin :
            if element not in carte[-2] :
                if len(carte) ==2 :
                    possible.append(element)
                elif element not in carte[-3]:
                    possible.append(element)
        if len(possible)==1:
            carte[-1].append(possible[0])
        else :
            cont = False
            print(possible)
            print("ERROR")
            carte = carte[:-1]
            break
print(carte)

def compute_bord (tile) :
    data =[
    tile[0], #up
    "".join([tile[k][len(tile[k])-1] for k in range(len(tile))]), #right
    "".join([tile[len(tile)-1][k] for k in range(len(tile)-1, -1, -1)]), #down
    "".join([tile[k][0] for k in range(len(tile)-1, -1, -1)]), #left
    ]
    return(deepcopy(data))

#On fait pivoter les tuiles pour etre aligné
reference = carte[0][0]
#On oriente correctement la tuile en haut à guache
tiles_description[reference] = rotate(tiles_description[reference])
tiles_description[reference] = rotate(tiles_description[reference])
tiles_description[reference] = rotate(tiles_description[reference])
tiles[reference]=compute_bord (tiles_description[reference] )

for ligne in range(len(carte)):
    if ligne > 0 :
        ##On tourne la première image
        reference =carte[ligne-1][0]
        bord = tiles[reference][2]
        faire_pivoter = carte[ligne][0]
        #On recheche le bord à aligner
        cpt = 0
        to_match =[ bord, "".join(bord[k] for k in range(len(bord)-1, -1,-1 ))]
        for k in tiles[faire_pivoter] :
            if k in to_match :
                break
            else :
                cpt+=1
        #On fait pivoter pour le mettre en postion 3
        nb_pivot = 4 - cpt 
        for k in range(nb_pivot):
            tiles_description[faire_pivoter] = rotate(tiles_description[faire_pivoter])
        tiles[faire_pivoter]=compute_bord (tiles_description[faire_pivoter] )
        #Si les bords sont identique, il faut flipper
        if bord == tiles[faire_pivoter][0] :
            tiles_description[faire_pivoter] = rotate(tiles_description[faire_pivoter])
            tiles_description[faire_pivoter] = flip(tiles_description[faire_pivoter])
            tiles_description[faire_pivoter] = rotate(tiles_description[faire_pivoter])
            tiles_description[faire_pivoter] = rotate(tiles_description[faire_pivoter])
            tiles_description[faire_pivoter] = rotate(tiles_description[faire_pivoter])
            tiles[faire_pivoter]=compute_bord (tiles_description[faire_pivoter] )       
    
    for tt in range(1, len(carte[ligne])):
        reference =carte[ligne][tt-1]
        bord = tiles[reference][1]
        faire_pivoter = carte[ligne][tt]
        #On recheche le bord à aligner
        cpt = 0
        to_match =[ bord, "".join(bord[k] for k in range(len(bord)-1, -1,-1 ))]
        for k in tiles[faire_pivoter] :
            if k in to_match :
                break
            else :
                cpt+=1
        #On fait pivoter pour le mettre en postion 3
        nb_pivot = 3 - cpt 
        for k in range(nb_pivot):
            tiles_description[faire_pivoter] = rotate(tiles_description[faire_pivoter])
        tiles[faire_pivoter]=compute_bord (tiles_description[faire_pivoter] )
        #Si les bords sont identique, il faut flipper
        if bord == tiles[faire_pivoter][3] :
            tiles_description[faire_pivoter] = flip(tiles_description[faire_pivoter])
            tiles[faire_pivoter]=compute_bord (tiles_description[faire_pivoter] )

carte_complete =[["" for k in range(len(carte[1]))] for i in range (len(carte))]
for i in range(len(carte)):
    for k in range(len(carte[i])) :
        carte_complete[i][k] = deepcopy(tiles_description[carte[i][k]])

for i in range(len(carte_complete)) :
    for j in range(len(carte_complete[i])) :
        carte_complete[i][j] = carte_complete[i][j][1:-1] 
        for k in range (len(carte_complete[i][j])) :
            carte_complete[i][j][k] = carte_complete[i][j][k][1:-1]
        
#On cacatène tout

carte_full  =[] 
for k in range(len(carte_complete)) :
    for i in range (len(carte_complete[k][0])) :
        st = ""
        for j in range(len(carte_complete[k])) :
            st+= carte_complete[k][j][i]
        carte_full.append(st)
print(carte_full) 
sea_monter = [
        [1,0],
        [2,1],
        [2,4],
        [1,5],
        [1,6],
        [2,7],
        [2,10],
        [1,11],
        [1,12],
        [2,13],
        [2,16],
        [1,17],
        [1,18],
        [0,18],
        [1,19],
    ]
def check_monster(image, i, j) :

    for position in sea_monter :
        if image[i +position[0]][j +position[1]] !="#":
            return (False)
    return True

cpt = 0

#carte_full = flip(carte_full)
#carte_full=rotate(carte_full)
#carte_full=rotate(carte_full)
#carte_full=rotate(carte_full)
#carte_full=rotate(carte_full)
for i in range(len(carte_full)-3):
    for j in range(len(carte_full) - 19):
        if check_monster(carte_full, i, j) :
            cpt += 1

print(cpt)
cptk =0
for line in carte_full :
    for k in line :
        if k =="#":
            cptk +=1
print(cptk - 15*cpt)