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

"""A map is made up of many territories, each of which must have an owner
and armies."""

class Territory:

    def __init__(self, territory_dictionary):
        self.name = territory_dictionary['name']
        self.max_units = territory_dictionary['maxunits']
        self.id = territory_dictionary['id']
        self.owner = None
        self.attackable_neighbors = {}
        self.defendable_neighbors = {}
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()