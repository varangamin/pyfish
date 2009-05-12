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

"""A continent represents a collection of territories that give a bonus when controlled by a single player."""

class Continent:
    
    def __init__(self, name, territories, bonus):
        self._name = name
        self._territories = territories
        assert bonus > 0, "The continent bonus must be greater than 0."
        self._bonus = bonus
        
    @property
    def name(self):
        """The name of the continent."""
        return self._name
    
    @property
    def territories(self):
        """A tuple of territories."""
        return self._territories
    
    @property
    def bonus(self):
        """When a single player controls all territories on a continent at the 
        beginning of his turn he will receive bonus armies."""
        return self._bonus
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()