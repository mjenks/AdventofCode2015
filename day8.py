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
def length_stringliteral(literal):
    return len(literal)
    
def length_memory(literal):
    #start with the number of char minus 2 for the double quotes
    numchar = len(literal) - 2
    char_list = list(literal)
    i = 0
    for charcter in char_list:
        if charcter == '\\':
            if char_list[i-1] == '\\': #can't go out of array because all start with "
                numchar = numchar
            elif char_list[i+1] == 'x':
                numchar -= 3
            else:
                numchar -=1
        i += 1
    return numchar
    

#solve part 1
def part1(puzzle_data):
    literals = []
    memory = []
    for literal in puzzle_data:
        literals.append(length_stringliteral(literal))
        memory.append(length_memory(literal))
        
    return sum(literals) - sum(memory)

#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
puzzle_path = "input_day8.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)