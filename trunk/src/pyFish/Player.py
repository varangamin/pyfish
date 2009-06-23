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

"""Represents a player in a game of Warfish."""

class Player:
        
    def __init__(self, player_dictionary):
        self.name = player_dictionary['name']
        self.is_turn = player_dictionary['isturn'] != 0
        self.active = player_dictionary['active'] != 0
        self.team_id = player_dictionary['teamid']
        self.reserve_units = player_dictionary['units']
        self.profile_id = player_dictionary['profileid']
        self.id = player_dictionary['id']
        self.cards = ()
        self.territories = {} 
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()