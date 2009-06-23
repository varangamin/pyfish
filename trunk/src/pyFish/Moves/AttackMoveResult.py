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

"""A concrete implementation of MoveResult for the results from an attack."""

from pyFish.Moves import MoveResult

class AttackMoveResult(MoveResult.MoveResult):

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

if __name__ == "__main__":
    import doctest
    doctest.testmod()