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

"""A map is made up of many territories, each of which must have an owner
and armies."""

class Territory:
    
    def __init__(self, name, neighbors, owner, armies):
        assert isinstance(name, str)
        self._name = name
        self._owner = owner
        self._neighbors = neighbors
        self._armies = armies

    def __init__(self, territoryDictionary):
        self._name = territoryDictionary['name']
        self._maxUnits = territoryDictionary['maxunits']
        self._id = territoryDictionary['id']
        
    @property
    def name(self):
        """The name of the territory."""
        return self._name
    
    @property
    def neighbors(self):
        """Each territory has a tuple of neighbor territories."""
        return self._neighbors
    
    @property
    def owner(self):
        """The owner of the territory."""
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        self._owner = owner
    
    @property
    def armies(self):
        """The number of armies on a territory."""
        return self._armies
    
    @armies.setter
    def armies(self, armies):
        self._armies = armies
        
    @property
    def maxUnits(self):
        """The max number of units allowed on the territory."""
        return self._maxUnits
    
    @property
    def id(self):
        """The id Warfish gives the territory."""
        return self._id
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()