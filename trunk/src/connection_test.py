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

import urllib.request
import json
from pyFish import Rules, Map, Game, Player

details_response = urllib.request.urlopen('http://216.169.106.90/war/services/rest?_method=warfish.tables.getDetails&gid=55808245&sections=board,rules,map,continents&_format=json')
details = json.loads(bytes.decode(details_response.read()))

state_response = urllib.request.urlopen('http://216.169.106.90/war/services/rest?_method=warfish.tables.getState&gid=55808245&scetions=cards,board,details,players,possibleactions&_format=json')
state = json.loads(bytes.decode(state_response.read()))
print(state)

map = Map.Map(details['_content']['map']['_content']['territory'], details['_content']['board']['_content']['border'], details['_content']['continents']['_content']['continent'])
rules = Rules.Rules(details['_content']['rules'])
players = {player_info['id'] : Player.Player(player_info) for player_info in state['_content']['players']['_content']['player']} 

game = Game.Game(55808245, map, players, rules)
print("Territories")
for continent_id, continent in game.map.continents.items():
    print(continent.name)
    for key, value in continent.territories.items():
        print(" " * 5 + key + ": " + value.name)        

print("Neighbors")
for territory_id, territory in game.map.territories.items():
    print(territory.name + " can attack")
    for attackable_neighbor_id, attackable_neighbor in territory.attackable_neighbors.items():
        print(" " * 5 + attackable_neighbor_id + ": " + attackable_neighbor.name)
    print(territory.name + " can be attacked by")
    for defendable_neighbor_id, defendable_neighbor in territory.defendable_neighbors.items():
        print(" " * 5 + defendable_neighbor_id + ": " + defendable_neighbor.name)

print("Players")        
for player_id, player in game.players.items():
    print("id: {0}, name: {1}".format(player.id, player.name))