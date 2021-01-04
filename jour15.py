# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 08:09:11 2020

@author: gverquiere
"""
from copy import deepcopy
input_str = []
depart = 0
with open ('input15.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))
print(input_str)

rule ={}

for line in input_str :
    if line == '' :
        break
    else :
        name = line.split(': ')[0]
        values = line.split(': ')[1]
        first = values.split(' or ')[0]
        second =  values.split(' or ')[1]
        rules =[
            [
                int(first.split('-')[0]),
                int(first.split('-')[1]),
                ],
            [
                int(second.split('-')[0]),
                int(second.split('-')[1]),
                ],
            ]
        rule[name] = deepcopy(rules)
nearby_ticket = []
start =False
for line in input_str :
    if start :
        nearby_ticket.append(line)
    if line == 'nearby tickets:' :
        start= True
cpt = 0

position = {}
for key in rule.keys() :
    position[key]=[k for k in range(len(nearby_ticket[0].split(',')))]

#Pour chaque ticket :
for ticket in nearby_ticket :
    ticket_state = True
    for value in ticket.split(',') :
        value = int(value)
        valid = False
        #On cherche une règle
        for key in rule.keys():
            if ((value >= rule[key][0][0]) and (value <= rule[key][0][1])) or ((value >= rule[key][1][0]) and (value <= rule[key][1][1])):
                valid = True
        if valid == False :
            cpt +=value
            ticket_state = False
    
    #PART 2
    if ticket_state :
        temp_state ={}
        for rules in rule.keys():
            temp_state[rules]=[]
            for k in range (len(ticket.split(','))) :
                value = int(ticket.split(',')[k])
            
                if ((value >= rule[rules][0][0]) and (value <= rule[rules][0][1])) or ((value >= rule[rules][1][0]) and (value <= rule[rules][1][1])):
                    temp_state[rules].append(k)
                        #print(temp_state)
                else :
                     if k in position[rules] :
                         position[rules].remove(k)

   
    
print( cpt)


# Type = 10
# Row = 5
# arrival_plateform = 2
# duration = 18
# arrival track = 9
# seat = 7
# zone =11
ticket = ['' for k in range(20)]
k = 1
while k <20 :
    for key in position.keys() :
        if len(position[key]) == k:
            for item in position[key] :
                if ticket [item] =='':
                    ticket [item] = key
    k+=1
print(ticket)
for pos in position.keys():
    if pos not in ticket :
        print(pos)
tycket =[197,173,229,179,157,83,89,79,193,53,163,59,227,131,199,223,61,181,167,191]
cpt = 1
for k in [3, 4, 12, 14, 15, 17] :
    cpt *= tycket[k]
print(cpt)
