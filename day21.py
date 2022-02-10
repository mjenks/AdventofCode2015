# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:47:11 2022

@author: mjenks
"""

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.split(':')
        name = line[0].strip()
        val = line[1].strip()
        stat = name, val
        data.append(stat)
    return dict(data)
    

#functions for part 1

#solve part 1
def part1(puzzle_data):
    return 0

#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
puzzle_path = "input_day21.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)