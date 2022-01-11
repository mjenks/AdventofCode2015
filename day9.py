# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 20:05:45 2022

@author: mjenks
"""

import itertools

#parse input
def parse(puzzle_input):
    data = []
    destinations = set()
    for line in puzzle_input:
        line = line.strip()
        path, distance = line.split(' = ')
        cities = path.split(' to ')
        trip = cities, distance
        destinations.add(cities[0])
        destinations.add(cities[1])
        data.append(trip)
    return data, destinations
    

#functions for part 1

#solve part 1
def part1(puzzle_data):
    paths, destinations = puzzle_data
    shortest_path = 0
    cities_list = list(destinations)
    #make a matrix of distances between cities
    distance_matrix = [[0 for i in cities_list] for j in cities_list]
    for path in paths:
        cities, dist = path
        distance_matrix[cities_list.index(cities[0])][cities_list.index(cities[1])] = dist
        distance_matrix[cities_list.index(cities[1])][cities_list.index(cities[0])] = dist
    possible_routes = list(itertools.permutations(cities_list))
    distance = 0
    for route in possible_routes:
        for i in range(len(route)-1):
            cityA = cities_list.index(route[i])
            cityB = cities_list.index(route[i+1])
            distance += int(distance_matrix[cityA][cityB])
        if (shortest_path != 0) and distance > shortest_path:
            distance = 0
        else:
            shortest_path = distance
            distance = 0
        
    return shortest_path

#functions for part 2

#solve part 2
def part2(puzzle_data):
    paths, destinations = puzzle_data
    longest_path = 0
    cities_list = list(destinations)
    #make a matrix of distances between cities
    distance_matrix = [[0 for i in cities_list] for j in cities_list]
    for path in paths:
        cities, dist = path
        distance_matrix[cities_list.index(cities[0])][cities_list.index(cities[1])] = dist
        distance_matrix[cities_list.index(cities[1])][cities_list.index(cities[0])] = dist
    possible_routes = list(itertools.permutations(cities_list))
    distance = 0
    for route in possible_routes:
        for i in range(len(route)-1):
            cityA = cities_list.index(route[i])
            cityB = cities_list.index(route[i+1])
            distance += int(distance_matrix[cityA][cityB])
        if distance > longest_path:
            longest_path = distance
        distance = 0
        
    return longest_path

#run and print solution 
puzzle_path = "input_day9.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)