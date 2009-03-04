class Map:
    
    def __init__(self, continents):
        self._continents = continents
        
    @property
    def continents(self):
        return self._continents