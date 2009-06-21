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
    def __init__(self, arguments):
        self._arguments = arguments
    
    @abc.abstractproperty
    def action_id(self):
        """The action for this move."""
        raise NotImplementedError()
    
    @abc.abstractproperty
    def execute(self):
        """Send a doMove request to Warfish."""
        raise NotImplementedError()
    
    @property
    def arguments(self):
        """A dictionary of arguments for the move. Each type of move has different arguments."""
        return self._arguments
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()