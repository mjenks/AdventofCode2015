# -*- coding: utf-8 -*-
"""
Created on Fri Jan 07 20:34:17 2022

@author: mjenks
"""

import string

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip()
        connection = line.split('->')
        opperation = connection[0].split()
        result = connection[1].strip()
        data.append((opperation, result))
    return data

#functions for part 1
def wire_index(wire):
    wire = list(wire)
    if len(wire) == 1:
        index = string.ascii_lowercase.index(wire[0])
    else:
        index = string.ascii_lowercase.index(wire[1]) + (string.ascii_lowercase.index(wire[0])+1)*26
    return index



#solve part 1
def part1(puzzle_data):
    #number of wires
    wires = [-1 for a in range(len(puzzle_data))]
    unused_data = []
    for line in puzzle_data:
        opr, res = line
        if len(opr) == 1:
            try:
                signal = int(opr[0])
            except:
                unused_data.append(line)
            else:
                index = wire_index(res)
                wires[index] = signal
        else:
            unused_data.append(line)
    while -1 in wires:
        
        #update puzzle_data to remove met conditions
        puzzle_data = unused_data
        unused_data = []
        
        for line in puzzle_data:
            opr, res = line
            if len(opr) == 1:
                if wires[wire_index(opr[0])] == -1:
                    unused_data.append(line)
                else:
                    wires[wire_index(res)] = wires[wire_index(opr[0])]
            elif len(opr) == 2:
                if wires[wire_index(opr[1])] == -1:
                    unused_data.append(line)
                else:
                    wires[wire_index(res)] = ~(wires[wire_index(opr[1])]) & 0xFFFF
            elif len(opr) == 3:
                try:
                    signal1 = int(opr[0])
                except: 
                    signal1 = wires[wire_index(opr[0])]
                    
                try: 
                    signal2 = int(opr[2])
                except:
                    signal2 = wires[wire_index(opr[2])]
                    
                if signal1 == -1:
                    unused_data.append(line)
                elif signal2 == -1:
                    unused_data.append(line)
                elif opr[1] == 'LSHIFT':
                    wires[wire_index(res)] = signal1 << signal2
                elif opr[1] == 'RSHIFT':
                    wires[wire_index(res)] = signal1 >> signal2
                elif opr[1] == 'AND':
                    wires[wire_index(res)] = signal1 & signal2
                elif opr[1] == 'OR':
                    wires[wire_index(res)] = signal1 | signal2
            
                    
    return wires[0]

#functions for part 2

#solve part 2
def part2(puzzle_data, solution1):
        #number of wires
    wires = [-1 for a in range(len(puzzle_data))]
    unused_data = []
    for line in puzzle_data:
        opr, res = line
        if len(opr) == 1:
            try:
                signal = int(opr[0])
            except:
                unused_data.append(line)
            else:
                index = wire_index(res)
                wires[index] = signal
        else:
            unused_data.append(line)
            
    wires[1] = solution1
    while -1 in wires:
        
        #update puzzle_data to remove met conditions
        puzzle_data = unused_data
        unused_data = []
        
        for line in puzzle_data:
            opr, res = line
            if len(opr) == 1:
                if wires[wire_index(opr[0])] == -1:
                    unused_data.append(line)
                else:
                    wires[wire_index(res)] = wires[wire_index(opr[0])]
            elif len(opr) == 2:
                if wires[wire_index(opr[1])] == -1:
                    unused_data.append(line)
                else:
                    wires[wire_index(res)] = ~(wires[wire_index(opr[1])]) & 0xFFFF
            elif len(opr) == 3:
                try:
                    signal1 = int(opr[0])
                except: 
                    signal1 = wires[wire_index(opr[0])]
                    
                try: 
                    signal2 = int(opr[2])
                except:
                    signal2 = wires[wire_index(opr[2])]
                    
                if signal1 == -1:
                    unused_data.append(line)
                elif signal2 == -1:
                    unused_data.append(line)
                elif opr[1] == 'LSHIFT':
                    wires[wire_index(res)] = signal1 << signal2
                elif opr[1] == 'RSHIFT':
                    wires[wire_index(res)] = signal1 >> signal2
                elif opr[1] == 'AND':
                    wires[wire_index(res)] = signal1 & signal2
                elif opr[1] == 'OR':
                    wires[wire_index(res)] = signal1 | signal2
            
                    
    return wires[0]

#run and print solution 
puzzle_path = "input_day7.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data, solution1)
print(solution1)
print(solution2)