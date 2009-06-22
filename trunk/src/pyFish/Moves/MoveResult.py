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
provides a simple interface for the results of moves."""

import abc

class MoveResult(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def __init__(self, id, unix_timestamp, player_id):
        self._id = id
        self._unix_timestamp = unix_timestamp
        self._player_id = player_id
    
    @property
    def id(self):
        """The id of the move."""
        return self._id
    
    @abc.abstractproperty
    def result_id(self):
        """The id of the move as it appears when getting the history."""
        raise NotImplementedError()
    
    @property
    def unix_timestamp(self):
        """The Unix timestamp for when the move was executed."""
        return self._unix_timestamp
    
    @property
    def player_id(self):
        """The id of the player that made the move."""
        return self._player_id            
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()