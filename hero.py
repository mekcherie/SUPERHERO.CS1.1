import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero: 
     def __init__(self, name, starting_health=100):
         self.abilities = list()
         self.armors = list()
         self.name = name
         self.starting_health = starting_health
         self.current_health = starting_health
         self.alive_status = True
         self.deaths = 0
         self.kills = 0
    
     def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
    
     def add_weapon(self, weapon):
        """Add weapon to abilities list.
        weapon: Weapon Object.
        """
        self.abilities.append(weapon)

     def add_armor(self, armor):
         '''Add armor to self.armors
            Armor: Armor Object
         '''
         self.armors.append(armor)

     def add_kill(self, num_kills=1):
        """Update self.kills by num_kills amount"""
        self.kills += num_kills
    
     def add_death(self, num_deaths=1):
        """Update deaths with num_deaths"""
        self.deaths += num_deaths

     def attack(self):
         '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
         '''
         total_damage = 0
         for ability in self.abilities:
             damage = ability.attack()
             total_damage += damage
         return total_damage

     def defend(self):
         '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
         '''
         total_block = 0
         for armor in self.armors:
             total_block += armor.block()
         return total_block
     def take_damage(self, damage):
         '''Updates self.current_health to reflect the damage minus the defense.'''
         self.current_health -= damage + self.defend()
         if self.current_health < 0:
             self.current_health = 0

     def is_alive(self):  
         '''Return True or False depending on whether the hero is alive or not.
         '''
         if self.current_health <= 0:
             return False
         else:
             return True

     def fight(self, opponent):  
         ''' Current Hero will take turns fighting the opponent hero passed in.
         '''
         if len(self.abilities) == 0 and len(opponent.abilities) == 0:
             print("Draw")
             return
         while self.is_alive() and opponent.is_alive():
             self.take_damage(opponent.attack())
             opponent.take_damage(self.attack())

             if self.is_alive() == False:
                 print(f"{opponent.name} wins!")
                 self.add_death(1)
                 opponent.add_kill(1)

             elif opponent.is_alive() == False:
                 self.add_kill(1)
                 opponent.add_death(1)
                 print(f"{self.name} wins!")



if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())