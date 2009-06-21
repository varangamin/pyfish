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

"""A concrete implementation of Move for attacks."""

import Move

class AttackMove(Move.Move):
    
    def __init__(self, id, from_territory, to_territory, number_of_units, is_continuous):
        self._from_territory = from_territory
        self._to_territory = to_territory
        self._number_of_units = number_of_units
        self._is_continous = is_continuous
        self.arguments['fromcid'] = from_territory.id
        self.arguments['tocid'] = to_territory.id
        self.arguments['numunits'] = str(number_of_units)
        self.arguments['continuous'] = '1' if is_continous else '0'
        super().__init__(id, self.action_id(), arguments) 
    
    @property
    def action_id(self):
        return 'attack'
    
    @property
    def execute(self):
        raise NotImplementedError()
    
    @property
    def from_territory(self):
        """The territory the attack is coming from."""
        return self._from_territory
    
    @property
    def to_territory(self):
        """The territory being attacked"""
        return self._to_territory
    
    @property
    def number_of_units(self):
        """Number of units to attack with. 1-3 for when is_continuous is false or 3+ for when true."""
        return self._number_of_units
    
    @property
    def is_continuous(self):
        """Is the attack continous? A continuous attack continues until the territory is captured or the specified number of units are lost."""
        return self._is_continous

if __name__ == "__main__":
    import doctest
    doctest.testmod()