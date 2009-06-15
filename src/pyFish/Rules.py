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

"""Warfish rules are highly customizable. The Rules class represents the rules
for a particular game."""

NONE, LIGHT, MODERATE, FOGGY, VERY, EXTREME = range(6) 
TURN_BASED, AUTO, BLIND_AT_ONCE = range(3)

class Rules:

    def __init__(self, rules_dictionary):
        """The following values in the dictionary are currently unknown and unmapped:
            * keeppossession - I think this deals with keeping possession when abandoning territories but I am not sure.
            * keeppossessiononexpire - I don't know how this differs from keeppossession
            * numpercountry - I don't know how this differs from maxpercountry"""
        self._num_attacks = rules_dictionary['numattacks']
        self._num_transfers = rules_dictionary['numtransfers']
        self._pre_transfers = rules_dictionary['pretransfer']
        self._damage_dice_attack = rules_dictionary['afdie']
        self._damage_dice_defend = rules_dictionary['dfdie']
        self._allow_abandon = rules_dictionary['allowabandon'] != 0
        self._card_scale = rules_dictionary['cardscale'].split(",")
        self._next_cards_worth = rules_dictionary['nextcardsworth'].split(",")
        self._num_reserves = rules_dictionary['numreserves']
        self._allow_return_to_attack = rules_dictionary['returntoattack'] != 0
        self._allow_return_to_placement = rules_dictionary['returntoplace'] != 0
        self._max_armies_per_country = rules_dictionary['maxpercountry']
        self._fog = rules_dictionary['fog']
        self._attack_die_sides = rules_dictionary['adie']
        self._defend_die_sides = rules_dictionary['ddie']
        self._is_blind_at_once_play = rules_dictionary['baoplay'] != 0
        self._is_team_game = rules_dictionary['teamgame'] != 0
        self._allow_team_transfer = rules_dictionary['teamtransfer'] != 0
        self._allow_continuous_attack = rules_dictionary['continuousattack'] != 0
        self._boot_time = rules_dictionary['boottime']
        self._is_card_capture = rules_dictionary['hascards'] != 0 #TODO: I am not positive that this is actually a setting for card capture. I need to play with it.
        self._allow_team_place_units = rules_dictionary['teamplaceunits'] != 0
        self._initial_unit_placement = rules_dictionary['uplace'] #I think this has to do with the initial unit placement mechanism used.
        self._card_sets_traded = rules_dictionary['cardsetstraded']
        
    @property
    def num_attacks(self):
        """The number of attacks that are allowed per turn.
        A value of -1 means an infinite number are allowed."""
        return self._num_attacks
    
    @property
    def num_transfers(self):
        """The number of transfers that are allowed per turn."""
        return self._num_transfers
    
    @property
    def pre_transfers(self):
        """Used in blind-at-once games. Pre-transfers are transfers before the attack phase."""
        return self._pre_transfers
    
    @property
    def damage_dice_attack(self):
        """Only used with damage dice. The attacker needs more than this value."""
        return self._damage_dice_attack
    
    @property
    def damage_dice_defend(self):
        """Only used with damage dice. The defender needs more than this value."""
        return self._damage_dice_defend
    
    @property
    def allow_abandon(self):
        """Whether players are allowed to abandon territories or not."""
        return self._allow_abandon
    
    @property
    def card_scale(self):
        """How card sets scale when traded in."""
        return self._card_scale
    
    @property
    def next_cards_worth(self):
        """What the next sets of cards are worth."""
        return self._next_cards_worth
    
    @property
    def num_reserves(self):
        """The number of armies that are allowed to be stored in reserve."""
        return self._num_reserves
    
    @property
    def allow_return_to_attack(self):
        """Whether or not you can return to the attack phase from transfer in turn-based play."""
        return self._allow_return_to_attack
    
    @property
    def allow_return_to_placement(self):
        """Whether or not you can return to the unit placement phase from the attack phase in turn-based play."""
        return self._allow_return_to_placement
    
    @property
    def max_armies_per_country(self):
        """The maximum number of armies you can have in one country. Warfish considers 65535 to be unlimited."""
        return self._max_armies_per_country
    
    @property
    def fog(self):
        """The fog level controls the what you can see on the board."""
        return self._fog
    
    @property
    def attack_die_sides(self):
        """The number of sides on the attack die."""
        return self._attack_die_sides
    
    @property
    def defend_die_sides(self):
        """The number of sides on the defend die."""
        return self._defend_die_sides
    
    @property
    def is_blind_at_once_play(self):
        """Whether this game is blind-at-once play or not."""
        return self._is_blind_at_once_play
    
    @property
    def is_team_game(self):
        """Is this game a team game or not?"""
        return self._is_team_game
    
    @property
    def allow_team_transfer(self):
        """Whether you are allowed to transfer armies to team member territories or not"""
        return self._allow_team_transfer
    
    @property
    def allow_continuous_attack(self):
        """Whether continuous attack is allowed or not. This is for games that limit the number of attacks per turn."""
        return self._allow_continuous_attack
    
    @property
    def boot_time(self):
        """The time in seconds required before you are allowed to boot a player."""
        return self._boot_time
    
    @property
    def is_card_capture(self):
        """Card capture refers to whether you get an opponents cards after eliminating them."""
        return self._is_card_capture
    
    @property
    def allow_team_place_units(self):
        """Whether you can place units on team member territories or not."""
        return self._allow_team_place_units
    
    @property
    def initial_unit_placement(self):
        """How units are initially place. The choices are turn based, automatic, and blind-at-once."""
        return self._initial_unit_placement
    
    @property
    def card_sets_traded(self):
        """How many card sets have been traded in so far."""
        return self._card_sets_traded
     
if __name__ == "__main__":
    import doctest
    doctest.testmod()