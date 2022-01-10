# -*- coding: utf-8 -*-
"""
Created on Fri Jan 07 11:10:53 2022

@author: mjenks
"""

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        data.append(line.strip())
    return data

#functions for part 1
def vowels(char_list):
    a = char_list.count('a')
    e = char_list.count('e')
    i = char_list.count('i')
    o = char_list.count('o')
    u = char_list.count('u')
    return (a + e + i + o + u)
    
def repeat(char_list):
    check = False
    for i in range(len(char_list)-1):
        if char_list[i] == char_list[i+1]:
            check = True
            break
    return check
    
#contain the strings ab, cd, pq, or xy
def forbidden(char_list):
    contains = False
    for i in range(len(char_list)-1):
        pair = char_list[i] + char_list[i+1]
        if (pair == 'ab') or (pair == 'cd') or (pair == 'pq') or (pair == 'xy'):
            contains = True
            break
    return contains
            
            
    
def isnice(code):
    nice = True
    code_list = list(code)
    #check the number of vowels
    if vowels(code_list) < 3:
        nice = False
    elif not repeat(code_list):
        nice = False
    elif forbidden(code_list):
        nice = False
         
    return nice

#solve part 1
def part1(puzzle_data):
    nice = 0
    naughty = 0
    for child in puzzle_data:
        if isnice(child):
            nice += 1
        else:
            naughty += 1
            
    return nice

#functions for part 2
#repeated pair of letters with no overlapping
def rule1(code):
    met = False
    for i in range(len(code)-3):
        pair = code[i] + code[i+1]
        for j in range(i+2, len(code)-1):
            test_pair = code[j] + code[j+1]
            if test_pair == pair:
                met = True
                break
        if met:
            break
    return met
        

#a letter that repeats with exactly one letter between them
def rule2(code):
    met = False
    for i in range(len(code)-2):
        if code[i] == code[i+2]:
            met = True
            break
    return met
    
def isnice2(child):
    code = list(child)
    nice = False
    if rule1(code) and rule2(code):
        nice = True
    return nice

#solve part 2
def part2(puzzle_data):
    nice = 0
    naughty = 0
    for child in puzzle_data:
        if isnice2(child):
            nice += 1
        else:
            naughty += 1
            
    return nice

#run and print solution 
puzzle_path = "input_day5.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)