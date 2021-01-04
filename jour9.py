# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 07:47:45 2020

@author: gverquiere
"""
input_str = []
cible = 0
with open ('input9.css', 'r') as f :
    for line in f :
        input_str.append(int(line.strip()))
        
for k in range (26, len(input_str)):
    is_valid = False
    sublist = input_str[k-25:k]
    for i in range(25):
        for j in range(i+1, 25):
            if sublist[i] + sublist[j] == input_str[k]:
                is_valid = True
    if not is_valid :
        print(input_str[k])
        cible = input_str[k]
        break
print(cible)
# for start in range(len(input_str)-1) :
#     for stop in range (start +1, len(input_str)):
#         substring  = input_str[start: stop]
#         if sum(substring) == cible :
#             print(start)
#             print(stop)
#             print(sum(substring))
            
#             print(substring[0] + substring[-1])
#             break



