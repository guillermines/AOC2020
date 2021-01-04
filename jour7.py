# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 07:45:36 2020

@author: gverquiere
"""
import os
from copy import deepcopy

input_str = []
with open ('input7.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))
        
print( input_str)

rules = {}
out_color = ['shiny gold']
cont = True
while cont:
    cont = False
    for row in input_str :
        for color_in in out_color :
            if  color_in in row :
                print(row)
                color = row.split(' bags contain')[0]
                if color != color_in :
                    if color not in out_color :
                        out_color.append(color)
                        cont = True
        
print(out_color)
print(len(out_color))
start=''
for row in input_str :
    if row.split(' bags contain')[0] == 'shiny gold':
        start = row
print(start)
def count_inside_bags (bag_color) :
    for row in input_str :
        if row.split(' bags contain ')[0] == bag_color:
            start = row
            rules = start.split(' bags contain ')[1]
            if rules =="no other bags." :
                return 0
            else :
                rules_dict={}
                #print(rules)
                rule_list = rules.split(', ')
                for rule in rule_list:
                    nb_bags = rule.split(' ')[0]
                    #print(rule)
                    #print("nb bags "+nb_bags)
                    color = ' '.join(rule.split(' ')[1:-1])
                    rules_dict[color]= int(nb_bags)
                nb_bags_total = 0
                for key in rules_dict.keys():
                    nb_bags_in = (count_inside_bags (key) + 1)*rules_dict[key]
                    nb_bags_total+=nb_bags_in
                return(nb_bags_total) 
print(count_inside_bags ('shiny gold'))     


