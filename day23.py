# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 13:12:28 2022

@author: mjenks
"""

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip()
        command = []
        inst = line[:3]
        command.append(inst)
        if len(line) == 5:
            reg = line[4]
            command.append(reg)
        elif len(line) > 7:
            reg = line[4]
            command.append(reg)
            sign = line[7]
            command.append(sign)
            steps = int(line[8:])
            command.append(steps)
        elif len(line) > 5:
            sign = line[4]
            command.append(sign)
            steps = int(line[5:])
            command.append(steps)
        data.append(command)
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
puzzle_path = "input_day23.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)