# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 08:48:32 2020

@author: gverquiere
"""
import math
import os
print(os.listdir())

input_str = []
with open ('input5.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))

def find_row(seat):
    row = [0,127]
    for k in range (0,7):
        if seat[k] =='F':
            row=[row[0],row[0] + math.floor((row[1]-row[0])/2)]

        elif seat[k] =='B':
            row=[row[0] +math.ceil((row[1]-row[0])/2), row[1]]
        else :
            print( 'Error')       
    return(row[0])

def find_seat(seat):
    row = [0,7]
    for k in range (7,7+3):
        if seat[k] =='L':
            row=[row[0],row[0] + math.floor((row[1]-row[0])/2)]
        elif seat[k] =='R':
            row=[row[0] +math.ceil((row[1]-row[0])/2), row[1]]    
        else :
            print( 'error')
    return(row[0])

def find_seat_number(seat) :
    return (find_row(seat) *8 + find_seat(seat))

nb_max = 0
for seat in input_str :
    seat_nb = find_seat_number(seat) 
    if seat_nb>nb_max:
        nb_max = seat_nb
print(nb_max)

all_seat =[]
for seat in input_str :
    seat_nb = find_seat_number(seat) 
    all_seat.append (seat_nb)
 
for seat in range (0, 816) :
    if not seat in all_seat :
        if seat - 1 in all_seat:
            if seat + 1 in all_seat:
                print(seat)
            
    