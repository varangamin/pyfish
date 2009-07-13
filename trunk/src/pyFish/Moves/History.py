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

"""This module is for processing the results from getHistory into objects."""

import abc

"""Abstract base class for each move in the history."""
class HistoryMove(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def __init__(self, id, unix_timestamp, player_id):
        self.id = id
        self.unix_timestamp = unix_timestamp
        self.player_id = player_id
    
    @abc.abstractproperty
    def result_id(self):
        """The id of the move as it appears when getting the history."""
        raise NotImplementedError()
    
"""The results from a past attack."""
class AttackHistoryMove(HistoryMove):

    def __init__(self, history_move_dictionary):
        self.border_mods = history_move_dictionary['m'] #m stands for border_mod, but I have no idea what that means
        self.attackers_lost = history_move_dictionary['al']
        self.defenders_lost = history_move_dictionary['dl']
        self.from_territory_id = history_move_dictionary['fcid']
        self.to_territory_id = history_move_dictionary['tcid']
        self.attack_dice = history_move_dictionary['ad']
        self.defend_dice = history_move_dictionary['dd']
        self.defending_player_id = history_move_dictionary['ds']
        super().__init__(history_move_dictionary['id'], history_move_dictionary['t'], history_move_dictionary['s'])
        
    @property
    def result_id(self):
        return 'a'

"""Describes a territory being captured."""
class CaptureHistoryMove(HistoryMove):
    
    def __init__(self, history_move_dictionary):
        self.captured_territory_id = history_move_dictionary['cid']
        self.captured_player_id = history_move_dictionary['ds']
        super().__init__(history_move_dictionary['id'], history_move_dictionary['t'], history_move_dictionary['s'])

    @property
    def result_id(self):
        return 'c'

"""Describes a player being eliminated."""
class EliminatePlayerHistoryMove(HistoryMove):
    
    def __init__(self, history_move_dictionary):
        self.eliminated_player_id = history_move_dictionary['es'] 
        super().__init__(history_move_dictionary['id'], history_move_dictionary['t'], history_move_dictionary['s'])

    @property
    def result_id(self):
        return 'e'


history_constructors = dict(a=AttackHistoryMove,
                            c=CaptureHistoryMove,
                            e=EliminatePlayerHistoryMove)

"""Turn the move history from the Warfish api call into a dictionary of move HistoryMove objects."""
def process_history(move_dictionary):
    """Process a dictionary of moves returned by making the getHistory Warfish API call."""
    history = []
    for item in move_dictionary:
        try:
            history.append(history_constructors[item['a']](item))
        except KeyError:
            print('{0} is not implemented yet. {1}'.format(item['a'], item))
    return history
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()