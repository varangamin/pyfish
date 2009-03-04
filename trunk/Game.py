class Game:
    
    def __init__(self, map, players):
        self._map = map
        self._players = players
        
    @property
    def map(self):
        return self._map
    
    @property
    def players(self):
        return self._players