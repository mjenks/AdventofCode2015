# -*- coding: utf-8 -*-
"""
Created on Thu Jan 06 20:33:06 2022

@author: mjenks
"""

#parse input
def parse(puzzle_input):
    data = list(puzzle_input)
    return data
    

#functions for part 1


#solve part 1
def part1(puzzle_data):
    #assume (0,0) start position turn directions into the locataions on grid
    x = 0
    y = 0
    stops = [(0,0)]
    for step in puzzle_data:
        #move
        if step == '^' :
            y += 1
        elif step == '>':
            x += 1
        elif step == 'v':
            y -= 1
        elif step == '<':
            x -= 1
        #store location
        stops.append((x,y))
        
    houses = set(stops)
            
        
    return len(houses)

#functions for part 2

#solve part 2
def part2(puzzle_data):
    #assume (0,0) start position turn directions into the locataions on grid
    x_s = 0
    y_s = 0
    stops_santa = [(0,0)]
    x_r = 0
    y_r = 0
    stops_robo = [(0,0)]
    i = 0
    for step in puzzle_data:
        i +=1
        #who moves
        if i%2 == 0:
            #move
            if step == '^' :
                y_s += 1
            elif step == '>':
                x_s += 1
            elif step == 'v':
                y_s -= 1
            elif step == '<':
                x_s -= 1
        #store location
            stops_santa.append((x_s,y_s))
        elif i%2 == 1:
            #move
            if step == '^' :
                y_r += 1
            elif step == '>':
                x_r += 1
            elif step == 'v':
                y_r -= 1
            elif step == '<':
                x_r -= 1
        #store location
            stops_robo.append((x_r,y_r))
            
    stops = stops_santa + stops_robo
        
    houses = set(stops)
            
        
    return len(houses)

#run and print solution 
puzzle_path = "input_day3.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)