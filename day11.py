# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 10:55:04 2022

@author: mjenks
"""
import string

#functions for part 1
def increment(pwd):
    old_pwd = list(pwd)
    iterating = True
    i = -1
    j = 0
    while iterating:
        if abs(i) == len(old_pwd):
            j = len(old_pwd)
            new_pwd = []
            while j > 0:
                new_pwd.append('a')
                j -= 1
            iterating = False
        elif old_pwd[i] == 'z':
            j += 1
        else:
            new_pwd = old_pwd[:i]
            letter = string.ascii_lowercase[string.ascii_lowercase.index(old_pwd[i]) + 1]
            new_pwd.append(letter)
            while j > 0:
                new_pwd.append('a')
                j -= 1
            iterating = False
        i -= 1

    return ''.join(new_pwd)

#solve part 1
def part1(puzzle_data):
    return 0

#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
puzzle_input = "hxbxwxba"
    
puzzle_data = puzzle_input
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)