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

"""A game of Warfish is represented by a series of moves."""

class Move:
    
    def __init__(self, action, arguments):
        """Creates a Move.
        
        >>> move = Move('join', {'colorid': '1', 'name': 'The Curmudgeon'})
        >>> print(move)
        &action=join&colorid=1&name=The Curmudgeon
        """
        self._action = action
        self._arguments = arguments
    
    def __str__(self):
        arguments_string = ""
        for key, value in self._arguments.items():
            arguments_string += "&{0}={1}".format(key, value) 
        return "&action=" + self._action + arguments_string
    
    @property
    def action(self):
        """The action for this move."""
        return self._action
    
    @property
    def arguments(self):
        """A dictionary of arguments for the move. Each type of move has different arguments."""
        return self._arguments
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()