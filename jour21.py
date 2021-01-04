# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 08:20:31 2020

@author: gverquiere
"""
from copy import deepcopy
input_str=[]
with open ('input21.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))

#Nettoyage des données
data = []
for line in input_str:
    ingredient = line.split(' (contains ')[0].split(' ')
    allergenes = line[:-1].split(' (contains ')[1].split(', ')
    data.append([deepcopy(ingredient), deepcopy(allergenes)])

#Pour chaque allergene, on regarde les recettes qui en contiennent
#On note tous les ingrédients qui peuvent la contenir
allergenes ={}
for line in data :
    for allergene in line[1] :
        if allergene not in allergenes.keys():
            allergenes[allergene]=[]
        allergenes[allergene].append(deepcopy(line[0]))

ingredient_alllergenes ={}
for allergene in allergenes.keys() :
    recettes = allergenes[allergene]
    ingredients_possibles = recettes[0]
    for recette in recettes:
        ingredient_to_remove = []
        for ingredient in ingredients_possibles :
            if ingredient not in recette :
                ingredient_to_remove.append(ingredient)
        for ing in ingredient_to_remove:
            ingredients_possibles.remove(ing)
    ingredient_alllergenes[allergene] = deepcopy(ingredients_possibles)



#On a la liste des ingrédients qui peuvent contenir un allergene
ingredient_to_remove =[]
for k in ingredient_alllergenes.keys():
    for ing in ingredient_alllergenes[k]:
        if ing not in ingredient_to_remove:
            ingredient_to_remove.append(ing)


cpt = 0
for line in data :
    for ing in line[0]:
        #if ing != '':
            if ing not in ingredient_to_remove :
                cpt +=1
print(cpt)
ingredient_allergenique ={}
for k in ingredient_alllergenes.keys():
    ingredient_alllergenes[k].sort()
    print(ingredient_alllergenes[k])
    for ing in ingredient_alllergenes[k] :
        if ing not in ingredient_allergenique.keys() :
            ingredient_allergenique[ing] =1
        else :
            ingredient_allergenique[ing] +=1
print(ingredient_allergenique)
            


