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

    def __init__(self, rulesDictionary):
        """The following values in the dictionary are currently unknown and unmapped:
            * keeppossession - I think this deals with keeping possession when abandoning territories but I am not sure.
            * keeppossessiononexpire - I don't know how this differs from keeppossession
            * numpercountry - I don't know how this differs from maxpercountry"""
        self._numAttacks = rulesDictionary['numattacks']
        self._numTransfers = rulesDictionary['numtransfers']
        self._preTransfers = rulesDictionary['pretransfer']
        self._damageDiceAttack = rulesDictionary['afdie']
        self._damageDiceDefend = rulesDictionary['dfdie']
        self._allowAbandon = rulesDictionary['allowabandon'] != 0
        self._cardScale = rulesDictionary['cardscale'].split(",")
        self._nextCardsWorth = rulesDictionary['nextcardsworth'].split(",")
        self._numReserves = rulesDictionary['numreserves']
        self._allowReturnToAttack = rulesDictionary['returntoattack'] != 0
        self._allowReturnToPlacement = rulesDictionary['returntoplace'] != 0
        self._maxArmiesPerCountry = rulesDictionary['maxpercountry']
        self._fog = rulesDictionary['fog']
        self._attackDieSides = rulesDictionary['adie']
        self._defendDieSides = rulesDictionary['ddie']
        self._isBlindAtOncePlay = rulesDictionary['baoplay'] != 0
        self._isTeamGame = rulesDictionary['teamgame'] != 0
        self._allowTeamTransfer = rulesDictionary['teamtransfer'] != 0
        self._allowContinuousAttack = rulesDictionary['continuousattack'] != 0
        self._bootTime = rulesDictionary['boottime']
        self._isCardCapture = rulesDictionary['hascards'] != 0 #TODO: I am not positive that this is actually a setting for card capture. I need to play with it.
        self._allowTeamPlaceUnits = rulesDictionary['teamplaceunits'] != 0
        self._initialUnitPlacement = rulesDictionary['uplace'] #I think this has to do with the initial unit placement mechanism used.
        self._cardSetsTraded = rulesDictionary['cardsetstraded']
        
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
    def nextCardsWorth(self):
        """What the next sets of cards are worth."""
        return self._nextCardsWorth
    
    @property
    def numReserves(self):
        """The number of armies that are allowed to be stored in reserve."""
        return self._numReserves
    
    @property
    def allowReturnToAttack(self):
        """Whether or not you can return to the attack phase from transfer in turn-based play."""
        return self._allowReturnToAttack
    
    @property
    def allowReturnToPlacement(self):
        """Whether or not you can return to the unit placement phase from the attack phase in turn-based play."""
        return self._allowReturnToPlacement
    
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
    
    @property
    def isBlindAtOncePlay(self):
        """Whether this game is blind-at-once play or not."""
        return self._isBlindAtOncePlay
    
    @property
    def isTeamGame(self):
        """Is this game a team game or not?"""
        return self._isTeamGame
    
    @property
    def allowTeamTransfer(self):
        """Whether you are allowed to transfer armies to team member territories or not"""
        return self._allowTeamTransfer
    
    @property
    def allowContinuousAttack(self):
        """Whether continuous attack is allowed or not. This is for games that limit the number of attacks per turn."""
        return self._allowContinuousAttack
    
    @property
    def bootTime(self):
        """The time in seconds required before you are allowed to boot a player."""
        return self._bootTime
    
    @property
    def isCardCapture(self):
        """Card capture refers to whether you get an opponents cards after eliminating them."""
        return self._isCardCapture
    
    @property
    def allowTeamPlaceUnits(self):
        """Whether you can place units on team member territories or not."""
        return self._allowTeamPlaceUnits
    
    @property
    def initialUnitPlacement(self):
        """How units are initially place. The choices are turn based, automatic, and blind-at-once."""
        return self._initialUnitPlacement
    
    @property
    def cardSetsTraded(self):
        """How many card sets have been traded in so far."""
        return self._cardSetsTraded
     
if __name__ == "__main__":
    import doctest
    doctest.testmod()