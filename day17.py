# -*- coding: utf-8 -*-
"""
Created on Fri Feb 04 20:26:42 2022

@author: mjenks
"""

import itertools

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        data.append(int(line.strip()))
    return data
    

#functions for part 1

#solve part 1
def part1(puzzle_data):
    nog = 150
    count = 0
    for i in range(1, len(puzzle_data)+1):
        #gives all combinations of i containers 
        comb = itertools.combinations(puzzle_data, i)
        for option in comb:
            if sum(option) == nog:
                count +=1
    
        
    return count

#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
puzzle_path = "input_day17.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)