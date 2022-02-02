# -*- coding: utf-8 -*-
"""
Created on Wed Feb 02 11:28:29 2022

MFCSAM output -

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

@author: mjenks
"""

#parse input
def parse(puzzle_input):
    return data

#functions for part 1

#solve part 1
def part1(puzzle_data):
    return 0

#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
puzzle_path = "input_day16.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)