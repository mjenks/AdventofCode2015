# -*- coding: utf-8 -*-
"""
Created on Fri Jan 07 10:44:57 2022

@author: mjenks
"""
import hashlib

#parse input
def parse(puzzle_input):
    data = puzzle_input.strip()
    return data

#functions for part 1

#solve part 1
def part1(puzzle_data):
    i = 0
    found = False
    while not found:
        code = puzzle_data + str(i)
        md5 = hashlib.md5(code.encode())
        hashcode = md5.hexdigest()
        if hashcode[:5] == '00000':
            found = True
            coin = i
        i +=1
        
    return coin

#functions for part 2

#solve part 2
def part2(puzzle_data):
    i = 0
    found = False
    while not found:
        code = puzzle_data + str(i)
        md5 = hashlib.md5(code.encode())
        hashcode = md5.hexdigest()
        if hashcode[:6] == '000000':
            found = True
            coin = i
        i +=1
        
    return coin

#run and print solution 
puzzle_path = "input_day4.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
#puzzle_data = 'abcdef'
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)