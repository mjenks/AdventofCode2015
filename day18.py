# -*- coding: utf-8 -*-
"""
Created on Sat Feb 05 15:59:29 2022

@author: mjenks
"""
# # is on . is off
# 0 for off 1 for on in data
#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        row_symb = list(line.strip())
        row = []
        for symb in row_symb:
            if symb == '#':
                row.append(1)
            else:
                row.append(0)
        data.append(row)
    
    return data
    

#functions for part 1
#A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
#A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
def update(grid):
    new_grid = [[0 for x in grid[0]] for y in grid]
    count = [[0 for x in grid[0]] for y in grid]
    end = len(grid) -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0:
                if j == 0:
                    count[i][j] = grid[i+1][j] + grid[i][j+1] + grid[i+1][j+1]
                elif j == end:
                    count[i][j] = grid[i+1][j] + grid[i][j-1] + grid[i+1][j-1]
                else:
                    count[i][j] = grid[i+1][j-1] + grid[i+1][j] + grid[i][j+1] + grid[i+1][j+1] + grid[i][j-1]
            elif i == end:
                if j == 0:
                    count[i][j] = grid[i-1][j] + grid[i][j+1] + grid[i-1][j+1]
                elif j == end:
                    count[i][j] = grid[i-1][j] + grid[i][j-1] + grid[i-1][j-1]
                else:
                    count[i][j] = grid[i-1][j-1] + grid[i-1][j] + grid[i][j+1] + grid[i-1][j+1] + grid[i][j-1]
            else:
                if j == 0:
                    count[i][j] = grid[i-1][j] + grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1]
                elif j == end:
                    count[i][j] = grid[i-1][j-1] + grid[i-1][j] + grid[i][j-1] + grid[i+1][j-1] + grid[i+1][j]
                else:
                    count[i][j] = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j-1] + grid[i][j+1] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
            if grid[i][j] == 1:
                if count[i][j] == 2 or count[i][j] == 3:
                    new_grid[i][j] = 1
            else:
                if count[i][j] == 3:
                    new_grid[i][j] = 1
                    
    return new_grid

#solve part 1
def part1(puzzle_data):
    
    return 0

#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
puzzle_path = "input_day18.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)