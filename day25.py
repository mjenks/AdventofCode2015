# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:37:48 2022

@author: mjenks
"""

#functions for part 1
def next_code(code):
    return (code * 252533) % 33554393
    
def code_num(loc):
    row, col = loc
    number = sum(range(1,col+1)) + sum(range(col,col+row-1))
    return number

#solve part 1
def part1(puzzle_data):
    code = 20151125
    for i in range(1,code_num(puzzle_data)):
        code = next_code(code)
    return code


#run and print solution 
puzzle_data = (2947, 3029) # (row, column) from my puzzle input

solution1 = part1(puzzle_data)
print(solution1)
