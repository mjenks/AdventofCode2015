# -*- coding: utf-8 -*-
"""
Created on Sun Feb 06 19:31:15 2022

@author: mjenks
"""

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input[:-2]:
        line = line.strip().split('=>')
        element = line[0]
        new = line[1]
        replacement = element, new
        data.append(replacement)
    molecule = puzzle_input[-1].strip()
        
    return data, molecule
    

#functions for part 1

#solve part 1
def part1(puzzle_data):
    return 0

#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
puzzle_path = "input_day19.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)