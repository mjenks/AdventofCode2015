# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:24:29 2022

@author: mjenks
"""

#parse input
def parse(puzzle_input):
    data = [line.split() for line in puzzle_input]
    #make a list of the guests
    people = set()
    for line in data:
        people.add(line[0])
    people = list(people)
    #make a matrix of the happiness of each seat pairing
    happiness = [[0 for i in range(len(people))] for j in range(len(people))]
    for line in data:
        x = people.index(line[0]) 
        person2 = ''.join(list(line[-1])[:-1])
        y = people.index(person2)
        if line[2] == 'lose':
            value = -1 * int(line[3])
        else:
            value = int(line[3])
        happiness[x][y] = value

    data = people, happiness
    return data
    

#functions for part 1

#solve part 1
def part1(puzzle_data):
    return 0

#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
puzzle_path = "input_day13.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)