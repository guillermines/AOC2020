# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 09:26:13 2020

@author: gverquiere
"""
input_str ='538914762'
circle = [int(k) for k in input_str]
circle = circle +[k for k in range(10, 1000001)]

for i in range(10000000) :
    selected_cup = [1,2,3]
    selected_label = [circle[k] for k in selected_cup]
    
    destination_cup = circle[0] - 1
    verify = False
    while not verify :
        verify = True
        if destination_cup <1 :
            destination_cup = 1000000
        if destination_cup in selected_label :
            verify = False
            destination_cup -=1
            
    circle.pop(3)
    circle.pop(2)
    circle.pop(1)
    destination_index = circle.index(destination_cup)
    if destination_index+1 < len(circle) :
        circle  = circle [:destination_index+1] + selected_label+ circle[destination_index+1:]
    else :
        circle  = circle [:destination_index+1] + selected_label
    f = circle.pop(0)
    circle.append(f)
    
index_1 = circle.index(1)
label_1 = circle[index_1 +1]
label_2 = circle[index_1 +2]

print(label_1, label_2, label_1 * label_2)
    
        
            