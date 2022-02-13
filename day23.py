# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 13:12:28 2022

@author: mjenks
"""

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip()
        command = []
        inst = line[:3]
        command.append(inst)
        if len(line) == 5:
            reg = line[4]
            command.append(reg)
        elif len(line) > 7:
            reg = line[4]
            command.append(reg)
            sign = line[7]
            command.append(sign)
            steps = int(line[8:])
            command.append(steps)
        elif len(line) > 5:
            sign = line[4]
            command.append(sign)
            steps = int(line[5:])
            command.append(steps)
        data.append(command)
    return data
    

#functions for part 1
def run(instructions, a, b):
    i = 0
    while i < len(instructions):
        command = instructions[i]
        inst = command[0]
        if inst == 'hlf': #halve the register
            if command[1] == 'a':
                a = a // 2
            elif command[1] == 'b':
                b = b // 2
            else:
                print "Invalid register"
            i += 1
        elif inst == 'tpl': #triple the register
            if command[1] == 'a':
                a = 3*a
            elif command[1] == 'b':
                b = 3*b
            else:
                print "Invalid register"
            i +=1
        elif inst == 'inc': #incriment register
            if command[1] == 'a':
                a += 1
            elif command[1] == 'b':
                b += 1
            else:
                print "Invalid register"
            i +=1
        elif inst == 'jmp': #jump
            if command[1] == '+':
                i += command[2]
            elif command[1] == '-':
                i -= command[2]
            else:
                print "Error"
                continue
        elif inst == 'jie': #jump if even
            if command[1] == 'a':
                if a%2 == 0:
                    if command[2] == '+':
                        i += command[3]
                    elif command[2] == '-':
                        i -= command[3]
                    else:
                        print "Error"
                        continue
                else:
                    i += 1
            elif command[1] == 'b':
                if b%2 == 0:
                    if command[2] == '+':
                        i += command[3]
                    elif command[2] == '-':
                        i -= command[3]
                    else:
                        print "Error"
                        continue
                else:
                    i += 1
            else:
                print "Invalid regisiter"
                i += 1
        elif inst == 'jio': #jump if one
            if command[1] == 'a':
                if a == 1:
                    if command[2] == '+':
                        i += command[3]
                    elif command[2] == '-':
                        i -= command[3]
                    else:
                        print "Error"
                        continue
                else:
                    i += 1
            elif command[1] == 'b':
                if b == 1:
                    if command[2] == '+':
                        i += command[3]
                    elif command[2] == '-':
                        i -= command[3]
                    else:
                        print "Error"
                        continue
                else:
                    i += 1
            else:
                print "Invalid regisiter"
                i += 1
        else:
            print "Unknown instruction"
            i += 1
        
    return a, b
    
#solve part 1
def part1(puzzle_data):
    a = 0
    b = 0
    return run(puzzle_data, a, b)

#functions for part 2

#solve part 2
def part2(puzzle_data):
    a = 1
    b = 0
    return run(puzzle_data, a, b)

#run and print solution 
puzzle_path = "input_day23.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)