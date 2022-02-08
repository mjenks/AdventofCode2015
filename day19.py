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
def stepBack(repl, mol):
    molecules = set()
    for replace in repl:
        old, new = replace
        find = mol.find(new)
        while find != -1:
            molecules.add(mol[:find] + old + mol[find+len(new):])
            find = mol.find(new, find + 1)
    
    return molecules

#minimun number of steps to go from e to the input molecule
#work backward from molecule
#find all molecules one step back
#check for e
#use a set of tested molecules to exclude repeats and longer paths
#solve part 2
def part2(puzzle_data):
    replacements, molecule = puzzle_data
    found_mols = {molecule}
    count = 0
    molecules = {molecule}
    while not ('e' in molecules):
        new_mols = set()
        for mol in molecules:
            new_mols = new_mols | stepBack(replacements, mol)
        count += 1
        molecules = new_mols - found_mols #stores a list of only new molecules one step back
        found_mols = found_mols | new_mols #add the new molecules to list of previously found ones
        print count
            
        
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