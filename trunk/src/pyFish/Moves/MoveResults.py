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

"""This module provides classes for the results of moves."""

import abc

class MoveResult(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def __init__(self, move_result_dictionary):
        self.result_code = move_result_dictionary['_content']['return']['code']
        self.result_message = move_result_dictionary['_content']['return']['msg']
        self.possible_actions = []
        for action in move_result_dictionary['_content']['return']['_content']['possibleactions']['_content']['action']:
            possible_actions.append(action['id'])

class AttackMoveResult(MoveResult):
    
    def __init__(self, move_result_dictionary, attack_move):
        """Takes the results from the given attack move and creates a result object."""
        #TODO: Finish implementing
        super().__init__(move_result_dictionary)
        self.attackers_lost = move_result_dictionary['_content']['return']['_content']['results']['totalattackerlosses']
        self.defenders_lost = move_result_dictionary['_content']['return']['_content']['results']['totaldefenderlosses']
        self.from_territory_id = attack_move.from_territory.id
        self.to_territory_id = attack_move.to_territory.id
        self.defending_player_id = attack_move.to_territory.owner.id

class PlaceUnitsMoveResult:
    
    def __init__(self, move_result_dictionary, place_units_move):
        super().__init__(move_result_dictionary)

class FreeTransferMoveResult:
    
    def __init__(self, move_result_dictionary, free_transfer_move):
        super().__init__(move_result_dictionary)

move_result_constructors = dict(attack=AttackMoveResult,
                                placeunits=PlaceUnitsMoveResult,
                                freetransfer=FreeTransferMoveResult) 

def process_move_result(move_result_dictionary, move):
    """After taking a move Warfish returns information about that move as json. This takes
    that information as a dictionary and transforms it into a MoveResult object."""
    result = None
    constructor = move_result_constructors.get(move.action_id)
    if constructor:
        result = constructor(move_result_dictionary, move)
    else:
        result = move_result_dictionary
    return result

        
if __name__ == "__main__":
    import doctest
    doctest.testmod()