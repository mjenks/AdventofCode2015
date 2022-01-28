# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:51:21 2022

@author: mjenks
"""


#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.split()
        ingredient = [line[0].strip(':'), int(line[2].strip(',')), int(line[4].strip(',')), int(line[6].strip(',')), int(line[8].strip(',')), int(line[10])]
        data.append(ingredient)
    return data
    

#functions for part 1

#solve part 1
def part1(puzzle_data):
    score = 0
    maximum = 0
    
    #score all recipe combinations and keep track of the max score
    #will only work for 4 ingredients as in this situation...
    for i in range(0,100):
        for j in range(0,100-i):
            for k in range(0, 100-i-j):
                l = 100-i-j-k
                capacity = i*puzzle_data[0][1] + j*puzzle_data[1][1] + k*puzzle_data[2][1] + l*puzzle_data[3][1]
                durability = i*puzzle_data[0][2] + j*puzzle_data[1][2] + k*puzzle_data[2][2] + l*puzzle_data[3][2]
                flavor = i*puzzle_data[0][3] + j*puzzle_data[1][3] + k*puzzle_data[2][3] + l*puzzle_data[3][3]
                texture = i*puzzle_data[0][4] + j*puzzle_data[1][4] + k*puzzle_data[2][4] + l*puzzle_data[3][4]
                if (capacity < 0 or durability < 0 or flavor < 0 or texture < 0):
                    score = 0
                else:
                    score = capacity*durability*flavor*texture
                maximum = max(maximum, score)
    
    return maximum

#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
puzzle_path = "input_day15.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)