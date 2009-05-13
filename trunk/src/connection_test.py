import urllib.request
import json

class Rules:

    def __init__(self, numAttacks, numTransfers):
        self._numAttacks = numAttacks
        self._numTransfers = numTransfers
        
    @property
    def numAttacks(self):
        """The number of attacks that are allowed per turn.
        A value of -1 means an infinite number are allowed."""
        return self._numAttacks
    
    @property
    def numTransfers(self):
        """The number of transfers that are allowed per turn."""
        return self._numTransfers
    

def as_rules(dct):
    if 'numattacks' in dct:
        return Rules(dct['numattacks'], dct['numtransfers'])
    return dct

response = urllib.request.urlopen('http://warfish.net/war/services/rest?_method=warfish.tables.getDetails&gid=55808245&_format=json')
html = response.read()
print(json.dumps(bytes.decode(html), sort_keys=True, indent=4))
rules = json.loads(bytes.decode(html), object_hook=as_rules)

print(rules['_content']['rules'].numAttacks)