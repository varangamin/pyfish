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

"""This file is for me to experiment with different json processing methods in Python."""

import urllib.request
import json
from pyFish import Rules
from pyFish import Map
from pyFish import Game
    
def build_game_objects(dct):
    if 'numattacks' in dct:
        return Rules.Rules(dct)
    if 'boardid' in dct:
        return Map.Map([])
    return dct

response = urllib.request.urlopen('http://216.169.106.90/war/services/rest?_method=warfish.tables.getDetails&gid=55808245&sections=board,rules,map,continents&_format=json')
html = response.read()
print(json.dumps(bytes.decode(html), sort_keys=True, indent=4))
details = json.loads(bytes.decode(html), object_hook=build_game_objects)

print(details)
map = details['_content']['board']
rules = details['_content']['rules'] 

game = Game.Game(55808245, map, [], rules)
print(game)
print(game.rules.numAttacks)
print(game.rules.cardScale)
game.rules.cardScale