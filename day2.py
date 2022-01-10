# -*- coding: utf-8 -*-
"""
Created on Thu Jan 06 11:41:08 2022

@author: mjenks
"""

#parse input
def parse(puzzle_input):
    puzzle_data = []
    #Each line is lxwxh
    for line in puzzle_input:
        line = line.strip()
        data = [int(item) for item in line.split('x')]
        puzzle_data.append(data)
    return puzzle_data

#functions for part 1
def calculate_area(gift):
    area = 2*gift[0]*gift[1] + 2*gift[1]*gift[2] + 2*gift[2]*gift[0]
    #area of the smallest side can be found by ordering the list
    gift.sort()
    area += gift[0]*gift[1]
    return area

#solve part 1
def part1(puzzle_data):
    needed = 0
    #each gift needs 2*l*w + 2*w*h + 2*h*l plus extra equal to the smallest side
    for gift in puzzle_data:
        needed += calculate_area(gift)
    return needed

#functions for part 2
def ribbon_needed(gift):
    #volume of gift
    volume = gift[0]*gift[1]*gift[2]
    #smallest perimeter
    gift.sort()
    perimeter = 2*gift[0]+2*gift[1]
    needed = perimeter + volume
    return needed

#solve part 2
def part2(puzzle_data):
    ribbon = 0
    for gift in puzzle_data:
        ribbon += ribbon_needed(gift)
    return ribbon

#run and print solution 
puzzle_path = "input_day2.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)