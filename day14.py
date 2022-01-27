# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 10:47:53 2022

@author: mjenks
"""

#parse input
def parse(puzzle_input):
    data = []
    #strip each reindeers input to name, speed, flight time, rest time
    for line in puzzle_input:
        line = line.split()
        reindeer = [line[0], int(line[3]), int(line[6]), int(line[13])]
        data.append(reindeer)
    return data

#functions for part 1
def traveled(deer, time):
    time_count = 0
    resting = False
    distance = 0
    while time_count < time:
        if not resting:
            if (time_count + deer[2]) <= time:
                distance += deer[1]*deer[2]
                time_count += deer[2]
                resting = True
            else:
                remaining = time - time_count
                distance += deer[1]*remaining
                time_count += remaining
        elif resting:
            time_count += deer[3]
            resting = False
    return distance

#solve part 1
#race ends at 2503 seconds
def part1(puzzle_data):
    race_time = 2503
    position = []
    for reindeer in puzzle_data:
        position.append(traveled(reindeer, race_time))
    return max(position)

#functions for part 2

#solve part 2
#adding additional stored values to each reindeer to be as follows
# [name, flight speed, flight time, rest time, position, points]
def part2(puzzle_data):
    for reindeer in puzzle_data:
        reindeer.append(0)
        reindeer.append(0)
    race_time = 2503
    #loop to move and score each reindeer for every second of the race
    for i in range(race_time):
        positions = []
        # move
        for deer in puzzle_data:
            #check if flying
            if (i % (deer[2] + deer[3])) < deer[2]:
                deer[4] += deer[1]
            positions.append(deer[4])
        #score
        for deer in puzzle_data:
            if deer[4] == max(positions):
                deer[5] += 1
    #list scores after race
    scores = []
    for deer in puzzle_data:
        scores.append(deer[5])
    
    return max(scores)

#run and print solution 
puzzle_path = "input_day14.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)