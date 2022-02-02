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
#dictionary to store mfcsam output
mfcsam = {"children": 3, 
          "cats": 7,
          "samoyeds": 2,
          "pomeranians": 3,
          "akitas": 0,
          "vizslas": 0,
          "goldfish": 5,
          "trees": 3,
          "cars": 2,
          "perfumes": 1}

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip()
        number = int((line.split()[1]).strip(':'))
        line = line.split(',')
        first = line[0].split()
        line[0] = ' '.join(first[2:])
        aunt = number, line
        data.append(aunt)
    return data

#functions for part 1
def isSender(sue):
    sender = True
    for attr in sue:
        attr = attr.split(':')
        name = attr[0].strip()
        value = int(attr[1])
        if value != mfcsam[name]:
            sender = False
            
    return sender
        
        

#solve part 1
def part1(puzzle_data):
    potentials = []
    for sue in puzzle_data:
        num, traits = sue
        if isSender(traits):
            potentials.append(num)
    
    return potentials

#for part 2 cats and trees are a lower limit 
# and pomeranians and goldfish are an upper limit
#functions for part 2
def isSender2(sue):
    sender = True
    for attr in sue:
        attr = attr.split(':')
        name = attr[0].strip()
        value = int(attr[1])
        if name == 'trees' or name == 'cats':
            if value <= mfcsam[name]:
                sender = False
        elif name == 'pomeranians' or name == 'goldfish':
            if value >= mfcsam[name]:
                sender = False
        elif value != mfcsam[name]:
            sender = False
            
    return sender

#solve part 2
def part2(puzzle_data):
    potentials = []
    for sue in puzzle_data:
        num, traits = sue
        if isSender2(traits):
            potentials.append(num)
    
    return potentials

#run and print solution 
puzzle_path = "input_day16.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)