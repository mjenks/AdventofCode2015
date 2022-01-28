# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:51:21 2022

@author: mjenks
"""

#define an ingredient class
class ingredient:
    def __init__(self, name, cap, dur, fla, tex, cal):
        self.name = name
        self.capacity = cap
        self.durability = dur
        self.flavor = fla
        self.texture = tex
        self.calories = cal

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.split()
        data.append(ingredient(line[0].strip(':'), int(line[2].strip(',')), int(line[4].strip(',')), int(line[6].strip(',')), int(line[8].strip(',')), int(line[10])))
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
puzzle_path = "input_day15.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
print(puzzle_data)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)