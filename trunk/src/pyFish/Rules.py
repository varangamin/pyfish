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
        self.num_attacks = rules_dictionary['numattacks']
        self.num_transfers = rules_dictionary['numtransfers']
        self.pre_transfers = rules_dictionary['pretransfer']
        self.damage_dice_attack = rules_dictionary['afdie']
        self.damage_dice_defend = rules_dictionary['dfdie']
        self.allow_abandon = rules_dictionary['allowabandon'] != 0
        self.card_scale = rules_dictionary['cardscale'].split(",")
        self.next_cards_worth = rules_dictionary['nextcardsworth'].split(",")
        self.num_reserves = rules_dictionary['numreserves']
        self.allow_return_to_attack = rules_dictionary['returntoattack'] != 0
        self.allow_return_to_placement = rules_dictionary['returntoplace'] != 0
        self.max_armies_per_country = rules_dictionary['maxpercountry']
        self.fog = rules_dictionary['fog']
        self.attack_die_sides = rules_dictionary['adie']
        self.defend_die_sides = rules_dictionary['ddie']
        self.is_blind_at_once_play = rules_dictionary['baoplay'] != 0
        self.is_team_game = rules_dictionary['teamgame'] != 0
        self.allow_team_transfer = rules_dictionary['teamtransfer'] != 0
        self.allow_continuous_attack = rules_dictionary['continuousattack'] != 0
        self.boot_time = rules_dictionary['boottime']
        self.is_card_capture = rules_dictionary['hascards'] != 0 #TODO: I am not positive that this is actually a setting for card capture. I need to play with it.
        self.allow_team_place_units = rules_dictionary['teamplaceunits'] != 0
        self.initial_unit_placement = rules_dictionary['uplace'] #I think this has to do with the initial unit placement mechanism used.
        self.card_sets_traded = rules_dictionary['cardsetstraded']
     
if __name__ == "__main__":
    import doctest
    doctest.testmod()