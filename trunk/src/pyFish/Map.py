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
    
    def __init__(self, mapDictionary, boardDictionary, continentsDictionary):
        self._territories = tuple((Territory.Territory(item) for item in mapDictionary))
        self._continents = tuple((Continent.Continent(item, self._territories) for item in continentsDictionary))
        
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