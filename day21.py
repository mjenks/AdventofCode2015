# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:47:11 2022

@author: mjenks
"""

#Shop
#==============================================================================
# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0
# 
# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5
# 
# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3
#==============================================================================

import itertools

#item has type, cost, damage, and armor
class item:
    """player equipable item"""
    
    def __init__(self, typ, cost, damage, armor):
        self.type = typ
        self.cost = cost
        self.dmg = damage
        self.arm = armor
        
#available items
Weapons = {
    'Dagger': item('weapon', 8, 4, 0),
    'Shortsword': item('weapon', 10, 5, 0),
    'Warhammer': item('weapon', 25, 6, 0),
    'Longsword': item('weapon', 40, 7, 0),
    'Greataxe': item('weapon', 74, 8, 0)
}
    
Armor = {
    'cloth': item('armor', 0, 0, 0),
    'Leather': item('armor', 13, 0, 1),
    'Chainmail': item('armor', 31, 0, 2),
    'Splintmail': item('armor', 53, 0, 3),
    'Bandedmail': item('armor', 75, 0, 4),
    'Platemail': item('armor', 102, 0, 5)
}

Ring = {
    'empty': item('ring', 0, 0, 0),
    'Dmg+1': item('ring', 25, 1, 0),
    'Dmg+2': item('ring', 50, 2, 0),
    'Dmg+3': item('ring', 100, 3, 0),
    'Def+1': item('ring', 20, 0, 1),
    'Def+2': item('ring', 40, 0, 2),
    'Def+3': item('ring', 80, 0, 3),
}

    
#player has equipment and health
class player:
    """player character"""
    
    def __init__(self):
        self.health = 100
        
    def equip(self, gear_set):
        self.weapon = Weapons[gear_set['weapon']]
        self.body = Armor[gear_set['armor']]
        self.ring1 = Ring[gear_set['left_ring']]
        self.ring2 = Ring[gear_set['right_ring']]
        self.gold_spent = self.weapon.cost + self.body.cost + self.ring1.cost + self.ring2.cost
    
    def damage(self):
        return self.weapon.dmg + self.ring1.dmg + self.ring2.dmg
        
    def armor(self):
        return self.body.arm + self.ring1.arm + self.ring2.arm
        
        

#parse input
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.split(':')
        name = line[0].strip()
        val = int(line[1].strip())
        stat = name, val
        data.append(stat)
    return dict(data)
    

#functions for part 1
#checks who would die first if boss returns true if player return false
def fight(player, boss):
    player_damage = max(player.damage() - boss['Armor'], 1)
    boss_damage = max(boss['Damage'] - player.armor(),1)
    player_time = boss['Hit Points'] // player_damage + min(1, boss['Hit Points']%player_damage)
    boss_time = player.health // boss_damage + min(1, player.health%boss_damage)
    if player_time <= boss_time:
        return True
    else:
        return False

#solve part 1
def part1(puzzle_data):
    boss = puzzle_data
    player1 = player()
    cheapest = 1000
    expensive = 0
    gear = {'weapon': Weapons.keys(),
            'armor': Armor.keys(),
            'left_ring': Ring.keys(),
            'right_ring': Ring.keys()}
    for gear_set in [dict(zip(gear, v)) for v in itertools.product(*gear.values())]:
        if gear_set['left_ring'] == gear_set['right_ring'] and gear_set['left_ring'] != 'empty':
            continue
        player1.equip(gear_set)
        if fight(player1, boss):
            cheapest = min(cheapest, player1.gold_spent)
        else: 
            expensive = max(expensive, player1.gold_spent)
        
    return cheapest, expensive

#functions for part 2


#run and print solution 
puzzle_path = "input_day21.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = part1(puzzle_data)
print(solution1)
print(solution2)