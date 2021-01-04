# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 08:37:56 2020

@author: gverquiere
"""

from copy import deepcopy

def read_lines(filename, allow_blanks = False):
    return [l.strip() for l in open(filename).readlines() if len(l.strip()) > 0 or allow_blanks]

input_str=[]
with open ('input19.css', 'r') as f :
    for line in f :
        input_str.append(str(line.strip()))
print(input_str)
rules ={}
for line in input_str :
    if line == '':
        break
    i = int(line.split(': ')[0])
    rule = line.split(': ')[1]
    rules[i]=rule
print(rules)

def rule_matches(rules, index):
    rule = rules[index]
    if rule[0] == 0:
        return [rule[1]]
    else:
        result = []
        for group in rule[1]:
            indices = [int(x) for x in group.split()]
            res = rule_matches(rules, indices[0])
            for i in indices[1:]:
                parts = rule_matches(rules, i)
                res  = [r + p for r in res for p in parts]
            result = result + res    
        return result
    return None


def matches_rule11(prefixes, suffixes, message):
    for p in prefixes:
        for s in suffixes:
            if len(message) < len(p) + len(s): 
                return False
            if message.startswith(p) and message.endswith(s):
                if len(message) == len(p) + len(s): 
                    return True
                elif matches_rule11(prefixes, suffixes, message[len(p):len(message)-len(s)]):
                    return True
    return False


def matches_rule8(prefixes, suffixes, message):
    for p in prefixes:
        if len(message) < len(p):
            return False 
        if message.startswith(p):
            if matches_rule11(prefixes, suffixes, message[len(p):]):
                return True
            elif matches_rule8(prefixes, suffixes, message[len(p):]):
                return True
    return False


def part1(rules, messages):
    ok = rule_matches(rules, 0)
    return sum([1 for m in messages if m in ok])


def part2(rules, messages):
    prefixes = rule_matches(rules, 42)
    suffixes = rule_matches(rules, 31)
    return sum([1 for m in messages if matches_rule8(prefixes, suffixes, m)])


def solution(file):
    print("Input: ", file)
    data = read_lines(file, True)

    rules = {}
    subs  = {}
    for i, line in enumerate(data):
        if len(line.strip()) == 0: 
            break
        r = line.split(':')  
        if len(r[1]) == 4:
            rules[int(r[0])] = [0, r[1][2]]
        else:
            rules[int(r[0])] = [1, r[1].split('|')]

    messages = data[i+1:]

    p1 = part1(rules, messages)
    print("Part1: ", p1)

    p2 = part2(rules, messages)
    print("Part2: ", p2)

solution("input19.css")