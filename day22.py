# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 22:30:48 2022

@author: mjenks
"""

#boss class with attack action
class Boss:
    """boss character"""
    
    def __init__(self, hit_points, damage):
        self.health = hit_points
        self.attack = damage
        
    def attack(self, player):
        player.health -= max(1, self.attack - player.armor)
        


#player as a class with spells as functions
class Wizard:
    """player character"""
    
    def __init__(self):
        self.health = 50
        self.mana = 500
        self.armor = 0
        self.shield_turns = 0
        self.poison_turns = 0
        self.recharge_turns = 0
        self.mana_spent = 0
        
    def turn_start(self, boss):
        #While shield is active, your armor is increased by 7.
        if self.shield_turns != 0:
            self.shield_turns -= 1
        else:
            self.armor = 0
            
        #At the start of each turn while poison is active, it deals the boss 3 damage.
        if self.poison_turns != 0:
            self.poison_turns -= 1
            boss.health -= 3
        
        #At the start of each turn while recharge is active, it gives you 101 new mana.
        if self.recharge_turns != 0:
            self.recharge_turns -= 1
            self.mana += 101
        
        
    def magic_missle(self, boss):
        #Magic Missile costs 53 mana. It instantly does 4 damage.
        self.mana -= 53
        self.mana_spent += 53
        boss.health -= 2
        
    def drain(self, boss):
        #Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
        self.mana -= 73
        self.mana_spent += 73
        self.health += 2
        boss.health -= 2
        
    def shield(self):
        #Shield costs 113 mana. It starts an effect that lasts for 6 turns. 
        #While shield is active, your armor is increased by 7.
        self.mana -= 113
        self.mana_spent += 113
        self.armor = 7
        self.shield_turns = 6
        
    def poison(self):
        #Poison costs 173 mana. It starts an effect that lasts for 6 turns. 
        self.mana -= 173
        self.mana_spent += 173
        self.poison_turns = 6
        
    def recharge(self):
        #Recharge costs 229 mana. It starts an effect that lasts for 5 turns. 
        self.mana -= 229
        self.mana_spent += 229
        self.recharge_turns = 5

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        val = int(line.split(':')[1].strip())
        data.append(val)
        
    boss = Boss(data[0],data[1])
    return boss
    

#functions for part 1

#solve part 1
def part1(puzzle_data):
    return 0
 
#functions for part 2

#solve part 2
def part2(puzzle_data):
    return 0

#run and print solution 
puzzle_path = "input_day22.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = part1(puzzle_data)
solution2 = part2(puzzle_data)
print(solution1)
print(solution2)