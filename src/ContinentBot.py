#Copyright 2009 Brian Meeker
#
#This file is part of pyFish.
#
#pyFish is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#pyFish is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with pyFish.  If not, see <http://www.gnu.org/licenses/>.

from pyFish import Core
from pyFish.Moves import *

#You must provide values for the following variables

#The id of the game the bot is to play. 
GAME_ID = '53420604'
#The name of the player in the game the bot will be playing for.
PLAYER_NAME = 'The Curmudgeon'
#The cookie the bot will use to authenticate as PLAYER_NAME
COOKIE = 'SESSID=21548ed928da03bb61bade292db94948; LAST=829925F678A3F7AB3A03F11EC9BCBB6800340380D4A4' 

"""This bot attempts to capture continents."""
class ContinentBot:
    
    def __init__(self, game_id, player_name, cookie):
        self.game = Core.initialize_game(game_id, cookie)
        self.player = None
        for player_id, player in self.game.players.items():
            if(player.name == player_name):
                self.player = player
                break
        
    def take_turn(self):
        continent_utilities = self.calculate_continent_utility()
        target_continent = max(continent_utilities, key = lambda a: continent_utilities.get(a))
        print("Target Continent: {0}".format(target_continent.name))
        
        """Execute a full turn."""
        while len(self.game.possible_actions) > 0:
            move_result = None
            if 'placeunits' in self.game.possible_actions:
                print('\r\nPlacing Units')
                placement_territory = self.find_placement_territory(target_continent)
                move_result = self.place_units(placement_territory)
            elif 'attack' in self.game.possible_actions:
                print('\r\nAttacking')
                attack_targets = self.find_attack_targets(target_continent)
                if len(attack_targets) > 0:
                    move_result = self.attack(attack_targets)
                else:
                    self.game.possible_actions.remove('attack')
            elif 'transfer' in self.game.possible_actions:
                print('\r\nSkipping Transfers')
                self.game.possible_actions.remove('transfer')
            elif 'endturn' in self.game.possible_actions:
                print('\r\nEnding Turn')
                self.game.execute_move(Moves.EndTurnMove())
                break
            else:
                print("\r\nNo valid move found")
            if move_result != None:
                self.game.possible_actions = move_result.possible_actions
                print(move_result)
        print("\r\nTurn Complete")
    
    def find_placement_territory(self, target_continent):
        """Look at all of the territories in the continent and see if the bot owns any of those territories neighbors."""
        for territory in target_continent.territories:
            for neighbor in territory.defendable_neighbors.values():
                if neighbor.owner == self.player:
                    return neighbor
        
        return None
    
    def place_units(self, placement_territory):
        """Places all units on the placement_territory."""
        place_units_move = Moves.PlaceUnitsMove({placement_territory: self.player.reserve_units})
        return self.game.execute_move(place_units_move)
    
    def find_attack_targets(self, target_continent):
        """Finds all territories that the bot controls with 4 or more armies and the neighbors that 
        can be attacked from that territory."""
        can_attack_from = {}
        for territory in self.player.territories:
            if territory.armies >= 4:
                for attackable_neighbor in territory.attackable_neighbors.values():
                    if attackable_neighbor.owner != self.player:
                        if territory not in can_attack_from:
                            can_attack_from[territory] = []
                        can_attack_from[territory].append(attackable_neighbor)
        return can_attack_from
    
    def attack(self, attack_targets):
        """Picks one of the attack_targets and attacks it continuously. It will also handle
        the free transfer after capturing a territory if needed."""
        for territory, attackable_neighbors in attack_targets.items():
            for neighbor in attackable_neighbors:
                attack_move = Moves.AttackMove(territory, neighbor, territory.armies-1, True)
                attack_move_result = self.game.execute_move(attack_move)
                if attack_move_result.captured and 'freetransfer' in attack_move_result.possible_actions:
                    #Move all but one of the remaining armies to the captured territory.
                    free_transfer_move = Moves.FreeTransferMove(territory.armies - 1)
                    free_transfer_move_result = self.game.execute_move(free_transfer_move) 
                return attack_move_result

    def calculate_continent_utility(self):
        """Naively calculates the value of each continent as 
        bonus - territories - total_access_points - total_neighbors - worst_neigbors + 2(territories_owned)
        This leans towards small, easy to defend territories and then weights them towards which ones you own the most of."""
        utilities = {}
        for continent in self.game.map.continents.values():
            access_points = set()
            neighbors = set()
            border_territories = {}
            territories_owned = 0
            print(continent.name)
            print("    Bonus: {0}".format(continent.bonus))
            print("    Number of territories: {0}".format(len(continent.territories)))
            for territory in continent.territories.values():
                if territory.owner == self.player:
                    territories_owned += 1
                for neighbor in territory.defendable_neighbors.values():
                    if neighbor not in continent.territories.values():
                        border_territories.setdefault(territory, 0)
                        border_territories[territory] = border_territories[territory] + 1
                        access_points.add(territory)
                        neighbors.add(neighbor)
            print("    Total Access Points: {0}".format(len(access_points)))
            print("    Total Neighbors: {0}".format(len(neighbors)))
            
            worst_neighbor_count = 0
            for territory, number_of_outside_neighbors in border_territories.items():
                if number_of_outside_neighbors > worst_neighbor_count:
                    worst_neighbor_count = number_of_outside_neighbors
            print("    Max outside neighbors: {0}".format(worst_neighbor_count))
            print("    Territories owned: {0}".format(territories_owned))
            
            #If we own all of the territories set the utility to the smallest possible number. TODO: How to properly do this in Python.
            utility = -1000
            if territories_owned != len(continent.territories):
                utility = continent.bonus - len(continent.territories) - len(access_points) - len(neighbors) - worst_neighbor_count + 2 * territories_owned
            print("    Utility: {0}".format(utility))
            utilities[continent] = utility
        return utilities
                    
            
bot = ContinentBot(GAME_ID, PLAYER_NAME, COOKIE)
bot.take_turn()