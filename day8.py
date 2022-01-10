# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 11:20:28 2022

@author: mjenks
"""

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        data.append(line.strip())
    return data
    

#functions for part 1
    

#solve part 1
def part1(puzzle_data):        
    return sum(len(line) - len(eval(line)) for line in puzzle_data)

#functions for part 2
def new_length(s):
    total = len(s) + 2 # plus 2 for the surrounding quotes
    #then add one for each \ and " in the original string
    total += s.count('\\') 
    total += s.count('"')
    return total

#solve part 2
def part2(puzzle_data):
    
    return sum(new_length(line) - len(line) for line in puzzle_data)

#run and print solution 
puzzle_path = "input_day8.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)