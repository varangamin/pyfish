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

"""Represents a player in a game of Warfish."""

class Player:
    
    def __init__(self, name):
        assert isinstance(name, str)
        self._name = name
        self._cards = ()
        self._territories = ()
        
    @property
    def name(self):
        """The player's name."""
        return self._name
    
    @property
    def cards(self):
        """The cards a player currently has. The only information a player has about 
        opponents cards is how many they have."""
        return self._cards
    
    @property
    def territories(self):
        """The territories the player currently controls."""
        return self._territories
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()