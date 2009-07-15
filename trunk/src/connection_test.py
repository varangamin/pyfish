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

"""This file is for me to experiment with different json processing methods in Python."""

from pyFish import Core
from pyFish.Moves import *

GAME_ID = '53420604'
COOKIE = 'SESSID=21548ed928da03bb61bade292db94948; LAST=829925F678A3F7AB3A03F11EC9BCBB6800340380D4A4'

game = Core.initialize_game(GAME_ID, COOKIE)

print(game.possible_actions)

#print("Territories")
#for continent_id, continent in game.map.continents.items():
#    print(continent.name)
#    for key, value in continent.territories.items():
#        print(" " * 5 + key + ": " + value.name)        
#
#print("Neighbors")
#for territory_id, territory in game.map.territories.items():
#    print("{0} has {1} armies and is owned by {2}.".format(territory.name, territory.armies, territory.owner.name if territory.owner != None else "Neutral"))
#    print(" " * 4 + territory.name + " can attack")
#    for attackable_neighbor_id, attackable_neighbor in territory.attackable_neighbors.items():
#        print(" " * 8 + attackable_neighbor_id + ": " + attackable_neighbor.name)
#    print(" " * 4 + territory.name + " can be attacked by")
#    for defendable_neighbor_id, defendable_neighbor in territory.defendable_neighbors.items():
#        print(" " * 8 + defendable_neighbor_id + ": " + defendable_neighbor.name)
#
#print("Players")        
#for player_id, player in game.players.items():
#    print("id: {0}, name: {1}".format(player.id, player.name))
#    
#print("History")
#for history_move_result in game.history:
#    print("id: {0}, timestamp: {1}, player_id: {2}, result_id: {3}".format(history_move_result.id, history_move_result.unix_timestamp, history_move_result.player_id, history_move_result.result_id))