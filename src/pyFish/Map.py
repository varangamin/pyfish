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
    
    def __init__(self, map_dictionary, board_dictionary, continents_dictionary):
        self._territories = {item['id'] : Territory.Territory(item) for item in map_dictionary}
        self._continents = {item['id'] : Continent.Continent(item, self._territories) for item in continents_dictionary}
        #Each board element has two ids. a is the attacking country and b is the defending country.
        for item in board_dictionary:
            territory_a = self._territories[item['a']]
            territory_b = self._territories[item['b']]
            territory_a.attackable_neighbors[territory_b.id] = territory_b
            territory_b.defendable_neighbors[territory_a.id] = territory_a
        
    @property
    def continents(self):
        """A tuple of continents."""
        return self._continents
    
    @property
    def territories(self):
        """All of the territories on the map."""
        return self._territories
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()