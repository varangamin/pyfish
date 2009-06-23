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

"""A map in Warfish is made up of territories, which can be organized into continents."""

import json
from pyFish import Territory
from pyFish import Continent

class Map:
    
    def __init__(self, map_dictionary, board_dictionary, continents_dictionary, board_state_dictionary, players_dictionary):
        self.territories = {item['id'] : Territory.Territory(item) for item in map_dictionary}
        self.continents = {item['id'] : Continent.Continent(item, self.territories) for item in continents_dictionary}
        #Each board element has two ids. a is the attacking country and b is the defending country.
        for item in board_dictionary:
            territory_a = self.territories[item['a']]
            territory_b = self.territories[item['b']]
            territory_a.attackable_neighbors[territory_b.id] = territory_b
            territory_b.defendable_neighbors[territory_a.id] = territory_a
        #Assign each territory an owner.
        for item in board_state_dictionary:
            #A playerid of -1 means the territory is neutral
            territory = self.territories[item['id']]
            if item['playerid'] != '-1':
                player = players_dictionary[item['playerid']]
                territory.owner = player
                player.territories[territory.id] = territory
            territory.armies = item['units']
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()