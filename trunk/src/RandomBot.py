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
        #Get every attackable territory.
        can_attack_from = {}
        for territory in self.player.territories.values():
            if territory.armies >= 4:
                for attackable_neighbor in territory.attackable_neighbors.values():
                    if attackable_neighbor.owner != self.player:
                        if territory not in can_attack_from:
                            can_attack_from[territory] = []
                        can_attack_from[territory].append(attackable_neighbor)

        for territory, attackable_neighbors in can_attack_from.items():
            for neighbor in attackable_neighbors:
                attack_move = Moves.AttackMove(territory, neighbor, territory.armies-1, True)
            
bot = RandomBot(GAME_ID, PLAYER_NAME, COOKIE)
bot.take_turn()