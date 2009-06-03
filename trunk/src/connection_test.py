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
    
def as_rules(dct):
    if 'numattacks' in dct:
        return Rules.Rules(dct['numattacks'], dct['numtransfers'])
    return dct

response = urllib.request.urlopen('http://warfish.net/war/services/rest?_method=warfish.tables.getDetails&gid=55808245&_format=json')
html = response.read()
print(json.dumps(bytes.decode(html), sort_keys=True, indent=4))
rules = json.loads(bytes.decode(html), object_hook=as_rules)

print(rules['_content']['rules'].numAttacks)
print(rules)