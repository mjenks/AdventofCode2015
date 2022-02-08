# -*- coding: utf-8 -*-
"""
Created on Sun Feb 06 19:31:15 2022

@author: mjenks
"""
import re

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input[:-2]:
        line = line.strip().split('=>')
        element = line[0].strip()
        new = line[1].strip()
        replacement = element, new
        data.append(replacement)
    molecule = puzzle_input[-1].strip()
        
    return data, molecule
    

#functions for part 1

#solve part 1
def part1(puzzle_data):
    replacements, molecule = puzzle_data
    new_mols = set()
    for replace in replacements:
        old, new = replace
        find = molecule.find(old)
        while find != -1:
            new_mols.add(molecule[:find] + new + molecule[find+len(old):])
            find = molecule.find(old, find + 1)
            
            
    
    return len(new_mols)

#functions for part 2
def elements(mol):
    elems = re.findall('[A-Z][^A-Z]*', mol)
    return elems


#minimun number of steps to go from e to the input molecule
# Rn Y Ar only appear on the outputs only in this order with 0 or more Ys
# e is only a start option
# solution will be number of total elements - number of Rn and Ar - twice the number of Y - 1
#solve part 2
def part2(puzzle_data):
    replacements, molecule = puzzle_data
    elems = elements(molecule)
    Rn = elems.count('Rn')
    Ar = elems.count('Ar')
    Y = elems.count('Y')
    count = len(elems) - Rn - Ar - 2*Y - 1
        
    return count

#run and print solution 
puzzle_path = "input_day19.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)