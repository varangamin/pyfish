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
        self.id = id
        self.unix_timestamp = unix_timestamp
        self.player_id = player_id
    
    @abc.abstractproperty
    def result_id(self):
        """The id of the move as it appears when getting the history."""
        raise NotImplementedError()
    
class AttackMoveResult(MoveResult):

    def __init__(self, move_result_dictionary):
        self.border_mods = move_result_dictionary['m'] #m stands for border_mod, but I have no idea what that means
        self.attackers_lost = move_result_dictionary['al']
        self.defenders_lost = move_result_dictionary['dl']
        self.from_territory_id = move_result_dictionary['fcid']
        self.to_territory_id = move_result_dictionary['tcid']
        self.attack_dice = move_result_dictionary['ad']
        self.defend_dice = move_result_dictionary['dd']
        self.defending_player_id = move_result_dictionary['ds']
        super().__init__(move_result_dictionary['id'], move_result_dictionary['t'], move_result_dictionary['s'])
        
    @property
    def result_id(self):
        return 'a'
            
constructors = dict(a=AttackMoveResult)

def process_history(move_dictionary):
    """Process a dictionary of moves returned by making the getHistory Warfish API call."""
    history = {}
    for item in move_dictionary:
        try:
            history[item['id']] = constructors[item['a']](item)
        except KeyError:
            print('{0} is not implemented yet. {1}'.format(item['a'], item))
    return history

        
if __name__ == "__main__":
    import doctest
    doctest.testmod()