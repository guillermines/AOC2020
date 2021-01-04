# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:08:14 2020

@author: gverquiere
"""
input_str = []
depart = 0
with open ('input13.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))
dic = {}
depart = int(input_str[0])
input_str = input_str[1].split(',')
for k in range(len(input_str)):
    if input_str[k] !='x' :
        dic[int(input_str[k])] = k
        
# print(dic)
# for k in dic.keys():
#     dic[k] -= 72
# print(dic)
# #Le timestamp est en 41 *x
# cont = True
# k = 17374729306
# k = int(100000000000000/ 863)
# while cont :
#     valid = True
#     k+=1
#     timestamp = 863*k
#     for bus in dic.keys():
#         passage_attendu = timestamp + dic[bus]
#         if not passage_attendu % bus == 0 :
#             valid = False
#             break
#     if valid :
#         cont = False
# print (timestamp)
        

# bus = 0
# waiting_time = 100
# for b in input_str :
#     w = (depart // b +1) * b - depart
#     if w < waiting_time :
#         waiting_time = w
#         bus = b
# print(waiting_time * bus)
# print(bus)
# print(waiting_time)

with open("input13.css", "r") as fp:
    lines = fp.readlines()
timestamp = int(lines[0][:-1])
bus_ids = [int(x) for x in lines[1].split(",") if x.isdigit()]

import numpy as np
timestamps = range(timestamp-50, timestamp+50)
valid = np.inf
diff = np.inf
bus_id = np.inf

for time in timestamps:
    for bus in bus_ids:
        if time%bus==0:
            d = abs(time-timestamp)
            if time>timestamp and d < diff:
                valid = time
                diff = d
                bus_id = bus

print(bus_id*(valid-timestamp))

LINES=lines
start = int(LINES[0])
busses = ["x" if x == "x" else int(x) for x in LINES[1].split(",")]

def part2():
    mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
    print(mods)
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    return val
print(part2())
