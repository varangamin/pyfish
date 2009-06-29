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

"""A game of Warfish is represented by a series of moves. This abstract base class
provides a simple interface for executing specific types of moves."""

import abc

class Move(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def __init__(self):
        self.arguments = {}
    
    @abc.abstractproperty
    def action_id(self):
        """The action for this move."""
        raise NotImplementedError()
    
    def to_query_string(self):
        """Create a query string containing the name of the move and its arguments."""
        query_string = '&{0}={1}'.format('action', self.action_id)
        for key, value in self.arguments.items():
            query_string += "&{0}={1}".format(key, value)
        return query_string

"""A concrete implementation of Move for attacks."""
class AttackMove(Move):
    
    def __init__(self, from_territory, to_territory, number_of_units, is_continuous):
        super().__init__()
        self.from_territory = from_territory
        self.to_territory = to_territory
        self.number_of_units = number_of_units
        self.is_continous = is_continuous
        self.arguments['fromcid'] = from_territory.id
        self.arguments['tocid'] = to_territory.id
        self.arguments['numunits'] = str(number_of_units)
        self.arguments['continuous'] = '1' if is_continuous else '0'
        
    @property
    def action_id(self):
        return 'attack'

"""A concrete implementation of Move for placing units in blind-at-once unit 
placement during game setup or in unit placement phase during a turn-based play turn. """
class PlaceUnitsMove(Move):
    
    def __init__(self, territory_ids=(), number_of_units=()):
        """A move to place units takes a list of territory ids and a matching list of the number of units to put onto each territory."""
        super().__init__()
        self.arguments['clist'] = territories_ids
        self.arguments['ulist'] = number_of_units
    
    @property
    def action_id(self):
        return 'placeunits'

        
if __name__ == "__main__":
    import doctest
    doctest.testmod()