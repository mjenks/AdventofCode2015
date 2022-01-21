# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 17:30:27 2022

@author: mjenks
"""


#parse input
#I am choosing to treat the json input as simply a list of characters
# because for part 1 only numbers in it matter
def parse1(puzzle_input):
    data = list(puzzle_input)    
    return data
    
#part 2 looks at features of the json encoding so json parsing is useful
def parse2(puzzle_input):
    return 0
    

#functions for part 1

#solve part 1
def part1(puzzle_data):
    temp_array = []
    for i in range(len(puzzle_data)):
        try:
            temp_array.append(int(puzzle_data[i]))
        except:
            if puzzle_data[i] == '-':
                temp_array.append(-2)
            else:
                temp_array.append(-1)
    numbers = []
    digit_list = []
    for num in temp_array:
        if num == -1:
            if len(digit_list) > 0:
                try:
                    numbers.append(int("".join(digit_list)))
                except:
                    print("just a dash")
            digit_list = []
        elif num == -2:
            digit_list.append('-')
        else:
            digit_list.append(str(num))
        
    return sum(numbers)

#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
puzzle_path = "input_day12.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data1 = parse1(puzzle_input)
solution1 = part1(puzzle_data1)
puzzle_data2 = parse2(puzzle_input)
solution2 = part2(puzzle_data2)
print(solution1)
print(solution2)