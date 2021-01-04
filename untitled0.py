# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:51:05 2020

@author: gverquiere
"""

import os
print(os.listdir())

expenses = []
with open ('input4.css', 'r') as f :
    for line in f :
        expenses.append(str(line.strip()))



# # for k in range (len(expenses)):
# #     for i in range (k+1,len(expenses)):
# #          for j in range (i+1,len(expenses)):
        
# #             if (expenses [k]+ expenses[i]+ expenses[j])==2020:
# #                 print((expenses [k]* expenses[i]* expenses[j]))
# def is_valid(string):
#     min_letter = int(string.split('-')[0])
#     max_letter = int(string.split('-')[1].split(' ')[0])
#     letter = string.split('-')[1].split(' ')[1][0]
#     password = string.split('-')[1].split(' ')[2]
#     nb_letter = password.count(letter)
#     # if (nb_letter <= max_letter) and (nb_letter >= min_letter):
#     #     return True
#     status_min = 0
#     if (len (password)>min_letter-1):
#         if (password[min_letter -1] == letter):
#             status_min = 1
#     status_max = 0
#     if (len (password)>max_letter-1):
#         if (password[max_letter -1] == letter):
#             status_max = 1
#     return (status_min + status_max) ==1
    
#     #print(min_letter, max_letter, letter, nb_letter)
# cpt =0
# for password in expenses :
#     if is_valid(password):
#         cpt +=1
#         print(password)
# print(cpt)



def find_number_tree(right, down):
    position =[right, down]
    cpt = 0
    while True:
        if position[0] >=len(expenses[0]):
            position[0] -=len(expenses[0])
        if position[1] >=len(expenses):
            return cpt
        
        if expenses[position[1]][position[0]]=='#':
            cpt+=1
        position[0]+= right
        position[1]+= down
        print (position)

# cpt = 1
# list_slope =[[1,1],[3,1],[5,1], [7,1],[1,2]]    
# for slope in list_slope:
#     cpt *= find_number_tree(slope[0], slope[1])

# print(cpt)


passport = ['']
for line in expenses :
    if len(line) :
        passport[-1] = passport[-1] + line
    else :
        passport.append('')

print(passport)
document = passport[0]
passport_dict = []
for document in passport :
    dic = {}
    for i in range (len(document)):
        if document[i] == ':':
            key = document[i-3: i]
            for k in range(i+1, len(document)):
                if document[k] == ':' :
                    value = document[i+1: k - 3]
                    dic[key]= value
                    break
                
                if document[k] == ' ' :
                    value = document[i+1: k]
                    dic[key]= value
                    break            
                if k == (len(document)-1):
                    value = document[i+1: k+1]
                    dic[key]= value
    passport_dict.append(dic)               

cpt =0
for passport in passport_dict :
    
    valid = True
    
    if not 'byr' in passport.keys() :
        valid = False
    if not 'iyr' in passport.keys() :
        valid = False
    if not 'eyr' in passport.keys() :
        valid = False
    if not 'hgt' in passport.keys() :
        valid = False    
    if not 'hcl' in passport.keys() :
        valid = False
    if not 'ecl' in passport.keys() :
        valid = False
    if not 'pid' in passport.keys() :
        valid = False
    if valid :
        
        value = int(passport['byr'])
        if (value <1920) or (value > 2002):
            valid = False
 
        value = int(passport['iyr'])
        if (value <2010) or (value > 2020):
            valid = False
        
        value = int(passport['eyr'])
        if (value <2020) or (value > 2030):
            valid = False
            
        unit = passport['hgt'][-2:]
        if unit == 'cm':   
            value =int(passport['hgt'][0:-2])
            if (value <150) or (value > 193):
                valid = False
        elif unit == 'in':   
            value =int(passport['hgt'][0:-2])
            if (value <59) or (value > 76):
                valid = False
        else:
            valid = False
            
        value = passport['hcl']
        if value[0] != '#' :
            valid = False
        for i in range (1, len(value)):
            if not value[i] in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'] :
                valid = False     
        if len (value) != 7 :
            valid = False
           
        value = passport['ecl']
        if not value in ['amb','blu','brn','gry','grn','hzl','oth'] :
            valid = False 
        
        value = passport['pid']
        if len (value) != 9 :
            valid = False
        for i in range (0, len(value)):
            if not value[i].isdecimal():
                valid = False
    if valid :
        cpt+=1
print(cpt)
# passport_valid = []
# cpt = 0
# for document in passport :
#     is_valid = True
#     for substring in ['byr:', 'iyr:','eyr:','hgt:','hcl:', 'ecl:', 'pid:']:
    
#         if document.find(substring) == -1:
#             is_valid = False
#         else :
#             if substring == 'byr:' and is_valid:
#                 index = document.find(substring)
#                 date = int(document[index + 4: index + 8])
#                 if (date < (1920) or (date > 2002) ):
#                     is_valid = False
#                     print('byr')
                    
#             if substring == 'iyr:' and is_valid:
#                 index = document.find(substring)
#                 date = int(document[index + 4: index + 8])
#                 if (date < (2010) or (date > 2020) ):
#                     is_valid = False   
#                 if (index + 8) < len(document)  :
#                     if document[index + 8].isdigit() :
#                         is_valid = False 
#                         print('iyr')
                    
#             if substring == 'eyr:' and is_valid:
#                 index = document.find(substring)
#                 date = int(document[index + 4: index + 8])
#                 if (date < (2020) or (date > 2030) ):
#                     is_valid = False  
#                 if (index + 8) < len(document)  :
#                     if document[index + 8].isdigit() :
#                         is_valid = False 
#                         print('eyr')
                    
#             if substring == 'hgt:' and is_valid:
#                 index = document.find(substring)
#                 unit_position = index + 4
                
#                 while (document[unit_position].isdigit()) and (unit_position < len (document) -1) :
                    
#                     unit_position += 1 
                    
#                 value = int(document[index + 4: unit_position])
#                 unit = str(document[unit_position: unit_position + 2])
#                 if unit == 'cm' :
#                     if (value < (150) or (value > 193) ):
#                         is_valid = False  
#                         print('hgt')
#                 elif unit == 'in' :
#                     if (value < (59) or (value > 76) ):
#                         is_valid = False   
#                         print('hgt')
#                 else :
#                     is_valid = False
#                     print('hgt')
                
                
#             if substring == 'hcl:' and is_valid:
#                 index = document.find(substring)
#                 value = str(document[index + 4: index + 4+ 7])
#                 if value [0] != '#' :
#                     is_valid = False 
#                 for i in range (1, len(value)):
#                     if not value[i] in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'] :
#                         is_valid = False
#                         print('hcl')
                        
#                 if len( document) >(index + 4+ 7):
#                     if document[index + 4+ 7] !=' ':
#                         if len( document) >(index + 4+ 7 + 3):
#                             if document[index + 4+ 7 + 3] != ':':
#                                 print('error')
#                                 is_valid = False
#                         else :
#                             is_valid = False


#             if substring == 'ecl:' and is_valid:
#                 index = document.find(substring)
#                 value = str(document[index + 4: index + 4+ 3])
#                 if not value in ['amb','blu','brn','gry','grn','hzl','oth'] :
#                     is_valid = False 
#                     print('ecl')

#             if substring == 'pid:' and is_valid:
#                 index = document.find(substring)
#                 value = str(document[index + 4: index + 4+ 9])
#                 for i in range (len(value)):
#                     if not value[i].isdigit():
#                         is_valid = False
#                         print('pid')
#                 if not value[0]=='0' :
#                     is_valid = False
#                 if (index + 4+ 9) <len(document) :
#                       if  document[index + 4+ 9].isdigit():
#                         is_valid = False  
#                         print('pid')
                    
#     if is_valid :
#         cpt+=1
        
# print(cpt) 
# print(len(passport))





