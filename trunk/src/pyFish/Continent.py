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

"""A continent represents a collection of territories that give a bonus when controlled by a single player."""

class Continent:
    
    def __init__(self, continent_dictionary, territories):
        self.name = continent_dictionary['name']
        self.id = continent_dictionary['id']
        self.bonus = continent_dictionary['units']
        self.territories = {}
        for id in continent_dictionary['cids'].split(','):
            for key, value in territories.items():
                if key == id:
                    self.territories[key] = value
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()