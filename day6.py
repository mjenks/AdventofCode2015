# -*- coding: utf-8 -*-
"""
Created on Fri Jan 07 12:07:19 2022

@author: mjenks
"""

#parse input
def parse(puzzle_input):
    data = []
    instruction = []
    for line in puzzle_input:
        line = line.strip()
        parts = line.split(',')
        first = parts[0].split()
        second = parts[1].split()
        third = parts[2]
        start_coord = (int(first[-1]), int(second[0]))
        end_coord = (int(second[-1]), int(third))
        #set action to 0 for off, 1 for on, and 2 for toggle
        if first[:-1] == ['turn', 'off']:
            action = 0
        elif first[:-1] == ['turn', 'on']:
            action = 1
        elif first[:-1] == ['toggle']:
            action = 2
        instruction.append(action)
        instruction.append(start_coord)
        instruction.append(end_coord)
        data.append(instruction)
        instruction = []
    return data
        

#functions for part 1
def turn_on(display, start, stop):
    x_start, y_start = start
    x_end, y_end = stop
    for i in range(y_start, y_end+1):
        for j in range(x_start, x_end+1):
            display[j][i] = 1
    
    return display
    
def turn_off(display, start, stop):
    x_start, y_start = start
    x_end, y_end = stop
    for i in range(y_start, y_end+1):
        for j in range(x_start, x_end+1):
            display[j][i] = 0
    
    return display
    
def toggle(display, start, stop):
    x_start, y_start = start
    x_end, y_end = stop
    for i in range(y_start, y_end+1):
        for j in range(x_start, x_end+1):
            state_toggle = (display[j][i]+1)%2
            display[j][i] = state_toggle
    
    return display

#solve part 1
def part1(puzzle_data):
    rows, cols = (1000, 1000)
    display = [[0 for i in range(cols)] for j in range(rows)]
    for step in puzzle_data:
        if step[0] == 0:
            display = turn_off(display, step[1], step[2])
        elif step[0] == 1:
            display = turn_on(display, step[1], step[2])
        elif step[0] == 2:
            display = toggle(display, step[1], step[2])
    total_on = sum(i.count(1) for i in display)
        
    return total_on

#functions for part 2
def turn_on2(display, start, stop):
    x_start, y_start = start
    x_end, y_end = stop
    for i in range(y_start, y_end+1):
        for j in range(x_start, x_end+1):
            display[j][i] += 1
    
    return display
    
def turn_off2(display, start, stop):
    x_start, y_start = start
    x_end, y_end = stop
    for i in range(y_start, y_end+1):
        for j in range(x_start, x_end+1):
            if display[j][i] > 0:
                display[j][i] -=1

    
    return display
    
def toggle2(display, start, stop):
    x_start, y_start = start
    x_end, y_end = stop
    for i in range(y_start, y_end+1):
        for j in range(x_start, x_end+1):
            display[j][i] += 2
    
    return display

#solve part 2
def part2(puzzle_data):
    rows, cols = (1000, 1000)
    display = [[0 for i in range(cols)] for j in range(rows)]
    for step in puzzle_data:
        if step[0] == 0:
            display = turn_off2(display, step[1], step[2])
        elif step[0] == 1:
            display = turn_on2(display, step[1], step[2])
        elif step[0] == 2:
            display = toggle2(display, step[1], step[2])
    brightness = sum(sum(i) for i in display)
        
    return brightness

#run and print solution 
puzzle_path = "input_day6.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)