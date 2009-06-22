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

from pyFish.Moves import MoveResult
from pyFish.Moves import AttackMoveResult

constructors = dict(a=AttackMoveResult.AttackMoveResult)

def process_history(move_dictionary):
    """Process a dictionary of moves returned by making the getHistory Warfish API call."""
    history = {}
    for item in move_dictionary:
        try:
            history[item['id']] = constructors[item['a']](item)
        except KeyError:
            print('{0} is not implemented yet. {1}'.format(item['a'], item))
    return history