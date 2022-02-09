# -*- coding: utf-8 -*-
"""
Created on Mon Feb 07 21:39:03 2022

@author: mjenks
"""
    

from functools import reduce

#functions for part 1
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#solve part 1
# number of presents is 10 times the sum of facotors of the house number
def part1(puzzle_data):
    house_num = 1
    presents = 10
    while presents < puzzle_data:
        house_num += 1
        presents = sum(factors(house_num))*10
    
    return house_num

#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
  
puzzle_data = 34000000
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)