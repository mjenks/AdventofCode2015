# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 22:30:48 2022

@author: mjenks
"""

import random

#boss class with attack action
class Boss:
    """boss character"""
    
    def __init__(self, hit_points, damage):
        self.health = hit_points
        self.damage = damage
        
    def attack(self, player):
        player.health -= max(1, self.damage - player.armor)
        


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
        
        
    def magic_missile(self, boss):
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
        
    def shield(self, boss):
        #Shield costs 113 mana. It starts an effect that lasts for 6 turns. 
        #While shield is active, your armor is increased by 7.
        self.mana -= 113
        self.mana_spent += 113
        self.armor = 7
        self.shield_turns = 6
        
    def poison(self, boss):
        #Poison costs 173 mana. It starts an effect that lasts for 6 turns. 
        self.mana -= 173
        self.mana_spent += 173
        self.poison_turns = 6
        
    def recharge(self, boss):
        #Recharge costs 229 mana. It starts an effect that lasts for 5 turns. 
        self.mana -= 229
        self.mana_spent += 229
        self.recharge_turns = 5
        
    def can_cast(self):
        self.spells = []
        if self.mana >= 73:
            self.spells.append(self.magic_missile)
            self.spells.append(self.drain)
        if self.mana >= 113 and self.shield_turns == 0:
            self.spells.append(self.shield)
        if self.mana >= 173 and self.poison_turns == 0:
            self.spells.append(self.poison)
        if self.mana >= 229 and self.recharge_turns == 0:
            self.spells.append(self.recharge)
        

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        val = int(line.split(':')[1].strip())
        data.append(val)
        
    return data
    

#functions for part 1
#boss fight true if player wins false if boss wins
def fight(player, boss):
    turn = 0
    while player.health > 0 and boss.health > 0:
        player.turn_start(boss)
        if boss.health <= 0:
            return True
        if turn%2 == 0:
            #player turn
            player.can_cast()
            #player loses if unable to cast
            if len(player.spells) == 0:
                return False
            #cast a random spell prioritizing poison and recharge
            if player.poison in player.spells and boss.health > 18:
                player.poison(boss)
            elif player.mana < 300 and player.recharge in player.spells and boss.health > 20:
                player.recharge(boss)
            else:
                cast = random.choice(player.spells)
                cast(boss)
        else:
            #boss turn
            boss.attack(player)
        turn += 1
    if player.health <= 0:
        return False
    else:
        return True
   
    

#solve part 1
def part1(puzzle_data):
    count = 0
    wins = 0
    least_mana = 10000
    while count < 100000:
        player = Wizard()
        boss = Boss(puzzle_data[0], puzzle_data[1])
        if fight(player, boss):
            least_mana = min(player.mana_spent, least_mana)
            wins += 1
        count +=1
        
    return least_mana, wins
 
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