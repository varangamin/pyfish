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

"""Warfish rules are highly customizable. The Rules class represents the rules
for a particular game."""

class Rules:

    def __init__(self, numAttacks, numTransfers):
        self._numAttacks = numAttacks
        self._numTransfers = numTransfers
        
    @property
    def numAttacks(self):
        """The number of attacks that are allowed per turn.
        A value of -1 means an infinite number are allowed."""
        return self._numAttacks
    
    @property
    def numTransfers(self):
        """The number of transfers that are allowed per turn."""
        return self._numTransfers
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()