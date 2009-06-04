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

class Rules:

    def __init__(self, rulesDictionary):
        """The following values in the dictionary are currently unknown and unmapped:
            * keeppossession - I think this deals with keeping possession when abandoning territories but I am not sure.
            * keeppossessiononexpire - I don't know how this differs from keeppossession"""
        self._numAttacks = rulesDictionary['numattacks']
        self._numTransfers = rulesDictionary['numtransfers']
        self._preTransfers = rulesDictionary['pretransfer']
        self._damageDiceAttack = rulesDictionary['afdie']
        self._damageDiceDefend = rulesDictionary['dfdie']
        self._allowAbandon = rulesDictionary['allowabandon'] != 0
        self._cardScale = rulesDictionary['cardscale'].split(",")
        self._numReserves = rulesDictionary['numreserves']
        self._allowReturnToAttack = rulesDictionary['returntoattack'] != 0
        self._maxArmiesPerCountry = rulesDictionary['maxpercountry']
        self._fog = rulesDictionary['fog']
        self._attackDieSides = rulesDictionary['adie']
        self._defendDieSides = rulesDictionary['ddie']
        
    @property
    def numAttacks(self):
        """The number of attacks that are allowed per turn.
        A value of -1 means an infinite number are allowed."""
        return self._numAttacks
    
    @property
    def numTransfers(self):
        """The number of transfers that are allowed per turn."""
        return self._numTransfers
    
    @property
    def preTransfers(self):
        """Used in blind-at-once games. Pre-transfers are transfers before the attack phase."""
        return self._preTransfers
    
    @property
    def damageDiceAttack(self):
        """Only used with damage dice. The attacker needs more than this value."""
        return self._damageDiceAttack
    
    @property
    def damageDiceDefend(self):
        """Only used with damage dice. The defender needs more than this value."""
        return self._damageDiceDefend
    
    @property
    def allowAbandon(self):
        """Whether players are allowed to abandon territories or not."""
        return self._allowAbandon
    
    @property
    def cardScale(self):
        """How card sets scale when traded in."""
        return self._cardScale
    
    @property
    def numReserves(self):
        """The number of armies that are allowed to be stored in reserve."""
        return self._numReserves
    
    @property
    def allowReturnToAttack(self):
        """Whether or not you can return to unit placement from the attack phase in turn-based play."""
        return self._allowReturnToAttack
    
    @property
    def maxArmiesPerCountry(self):
        """The maximum number of armies you can have in one country. Warfish considers 65535 to be unlimited."""
        return self._maxArmiesPerCountry
    
    @property
    def fog(self):
        """The fog level controls the what you can see on the board."""
        return self._fog
    
    @property
    def attackDieSides(self):
        """The number of sides on the attack die."""
        return self._attackDieSides
    
    @property
    def defendDieSides(self):
        """The number of sides on the defend die."""
        return self._defendDieSides
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()