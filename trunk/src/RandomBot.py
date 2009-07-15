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

GAME_ID = '53420604'
PLAYER_NAME = 'The Curmudgeon'
COOKIE = 'SESSID=21548ed928da03bb61bade292db94948; LAST=829925F678A3F7AB3A03F11EC9BCBB6800340380D4A4'

class RandomBot:
    
    def __init__(self, game_id, player_name, cookie):
        self.game = Core.initialize_game(game_id, cookie)
        self.player = None
        for player_id, player in self.game.players.items():
            if(player.name == player_name):
                self.player = player
                break
        
    def take_turn(self):
        
        while True:
            move_result = None
            if 'placeunits' in self.game.possible_actions:
                move_result = self.place_units()
            elif 'attack' in self.game.possible_actions:
                attack_targets = self.find_attack_targets()
                if len(attack_targets) > 0:
                    move_result = self.attack(attack_targets)
                else:
                    self.game.possible_actions.remove('attack')
            elif 'transfer' in self.game.possible_actions:
                self.game.possible_actions.remove('transfer')
            elif 'endturn' in self.game.possible_actions:
                self.game.execute_move(Moves.EndTurnMove())
                break
            else:
                print("No valid move found")
            if move_result != None:
                self.game.possible_actions = move_result.possible_actions
                print(move_result)
    
    def place_units(self):
        remaining_units = self.player.reserve_units
        place_units_move = Moves.PlaceUnitsMove()
        while remaining_units > 0:
            for territory in self.player.territories:
                place_units_move.territory_ids.append(territory.id)
                place_units_move.number_of_units.append('1')
                remaining_units -= 1
                if remaining_units == 0:
                    break
        return self.game.execute_move(place_units_move)
    
    def find_attack_targets(self):
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
        #Get every attackable territory.
        for territory, attackable_neighbors in attack_targets.items():
            for neighbor in attackable_neighbors:
                attack_move = Moves.AttackMove(territory, neighbor, territory.armies-1, True)
                return self.game.execute_move(attack_move)
            
bot = RandomBot(GAME_ID, PLAYER_NAME, COOKIE)
bot.take_turn()