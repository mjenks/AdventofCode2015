# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 11:12:02 2022

@author: mjenks
"""


#functions for part 1
#takes a list of digits and returns a list of digits following look and say rules
def look_say(digits):
    new_number = []
    num = digits[0]
    count = 1
    for i in range(1,len(digits)):
        if digits[i] == digits[i-1]:
            count += 1
        else:
            new_number.append(count)
            new_number.append(num)
            num = digits[i]
            count = 1
    new_number.append(count)
    new_number.append(num)
    return new_number
            
        
        

#solve 
def play(puzzle_data, iterations):
    number = list(map(int, str(puzzle_data)))
    for i in range(iterations):
        number = look_say(number)
        
    return len(number)




#run and print solution     
    
puzzle_data = 1321131112
solution1 = play(puzzle_data, 40)
solution2 = play(puzzle_data, 50)
print(solution1)
print(solution2)