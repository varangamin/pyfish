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
    
    def __init__(self, name):
        assert isinstance(name, str)
        self._name = name
        self._cards = ()
        self._territories = {}
        
    def __init__(self, player_dictionary):
        self._name = player_dictionary['name']
        self._is_turn = player_dictionary['isturn'] != 0
        self._active = player_dictionary['active'] != 0
        self._team_id = player_dictionary['teamid']
        self._reserve_units = player_dictionary['units']
        self._profile_id = player_dictionary['profileid']
        self._id = player_dictionary['id']
        self._cards = ()
        self._territories = {}
        
    @property
    def id(self):
        """The player's id"""
        return self._id
    
    @property
    def name(self):
        """The player's name."""
        return self._name
    
    @property
    def cards(self):
        """The cards a player currently has. The only information a player has about 
        opponents cards is how many they have."""
        return self._cards
    
    @property
    def territories(self):
        """The territories the player currently controls."""
        return self._territories
    
    @property
    def is_turn(self):
        """Is it this player's turn?"""
        return self._is_turn
    
    @property
    def active(self):
        """Is this player still in the game?"""
        return self._active;
    
    @property
    def team_id(self):
        """If this is a team game this will be the id of the team the player is on.
        If it is not a team game it will be -1."""
        return self._team_id
    
    @property
    def reserve_units(self):
        """The number of reserve units this player has."""
        return self._reserve_units
    
    @property
    def profile_id(self):
        """Every player must have a registered Warfish account. This is the players Warfish id."""
        return self._profile_id 
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()