# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 10:55:04 2022

@author: mjenks
"""
import string

#functions for part 1
#function to increment password by one letter
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
    
#check if password meets the first requirement (3 consective letters)
def rule1(pwd):
    pwd = list(pwd)
    for i in range(len(pwd) - 2):
        one = string.ascii_lowercase.index(pwd[i])
        two = string.ascii_lowercase.index(pwd[i+1])
        three = string.ascii_lowercase.index(pwd[i+2])
        if (one + 1) == two and (three -1) == two:
            return True
        
    return False
    
#check if password meets second requirement (no i o or l)
def rule2(pwd):
    i = 'i' in pwd
    o = 'o' in pwd
    l = 'l' in pwd
    return not(i) and not(o) and not(l)
    
    
#check if password meets third requirement (two different non overlapping pairs)
def rule3(pwd):
    pwd = list(pwd)
    count = 0
    letters = set()
    for i in range(len(pwd)-1):
        if pwd[i] == pwd[i+1]:
            count += 1
            letters.add(pwd[i])
    if (count > 1) and (len(letters) > 1):
        return True
        
    return False
    

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