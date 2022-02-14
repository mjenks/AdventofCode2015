# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:37:29 2022

@author: mjenks
"""

import itertools

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        w = int(line.strip())
        data.append(w)
    return data
    

#functions for part 1
def entangle(group):
    qe = 1
    for w in group:
        qe = qe*w
    return qe


#solve part 1
def part1(puzzle_data):
    total_weight = sum(puzzle_data)
    group_weight = total_weight/3
    options = set() #will hold all the groups of gifts with the correct weight
    min_grp = group_weight//puzzle_data[-1]
    for i in range(min_grp,len(puzzle_data)//3): #smallest group can't have more than 1/3 
        for j in itertools.combinations(puzzle_data, i):
            if sum(j) == group_weight:
                options.add(j)
    smallest_group = min(len(x) for x in options)
    qe = []
    for group in options:
        if len(group) == smallest_group:
            qe.append(entangle(group))
            
    return min(qe)

#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
puzzle_path = "input_day24.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)