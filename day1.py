# -*- coding: utf-8 -*-
"""
Created on Thu Jan 06 10:54:21 2022

@author: mjenks
"""


#parse input
def parse(puzzle_input):
    data = list(puzzle_input)
    return data

#functions for part 1

#solve part 1
def part1(puzzle_data):
    floor = 0
    for char in puzzle_data:
        if (char == '('):
            floor += 1
        elif (char == ')'):
            floor -= 1
            
    return floor

#functions for part 2

#solve part 2
def part2(puzzle_data):
    floor = 0
    position = 0
    for char in puzzle_data:
        position += 1
        if (char == '('):
            floor += 1
        elif (char == ')'):
            floor -= 1
        if floor < 0:
            break            
        
    return position

#run and print solution 
puzzle_path = "input_day1.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)