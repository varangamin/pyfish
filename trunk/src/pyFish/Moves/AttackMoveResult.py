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
        self._border_mods = move_result_dictionary['m'] #m stands for border_mod, but I have no idea what that means
        self._attackers_lost = move_result_dictionary['al']
        self._defenders_lost = move_result_dictionary['dl']
        self._from_territory_id = move_result_dictionary['fcid']
        self._to_territory_id = move_result_dictionary['tcid']
        self._attack_dice = move_result_dictionary['ad']
        self._defend_dice = move_result_dictionary['dd']
        self._defending_player_id = move_result_dictionary['ds']
        super().__init__(move_result_dictionary['id'], move_result_dictionary['t'], move_result_dictionary['s'])
        
    @property
    def result_id(self):
        return 'a'
    
    @property
    def border_mods(self):
        """I have no clue what a border mod is."""
        return self._border_mods
    
    @property
    def attackers_lost(self):
        """The number of attacking units lost."""
        return self._attackers_lost
    
    @property
    def defenders_lost(self):
        """The number of defending units lost."""
        return self._defenders_lost
    
    @property
    def from_territory_id(self):
        """The id of the territory the attack came from."""
        return self._from_territory_id
    
    @property
    def to_territory_id(self):
        """The id of the territory that was being attacked."""
        return self._to_territory_id
    
    @property
    def attack_dice(self):
        """The result of the attackers roll as a comma separated list, such as '5,2,1'."""
        return self._attack_dice
    
    @property
    def defend_dice(self):
        """The result of the defenders roll as a comma separated list, such as '5,2'."""
        return self._defend_dice
    
    @property
    def defending_player_id(self):
        """The id of the player who was being attacked."""
        return self._defending_player_id

if __name__ == "__main__":
    import doctest
    doctest.testmod()