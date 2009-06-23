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

"""Represents a Warfish game. This is currently limited to only supporting 
a standard game of Risk. While Warfish allows customization of rules this is not currently supported."""

class Game:
    
    def __init__(self, id, map, players, rules):
        """Initializes a game with the given map and players."""
        self.id = id
        self.map = map
        self.players = players
        self.rules = rules
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()