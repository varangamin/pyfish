class Continent:
    
    def __init__(self, name, territories, bonus):
        self._name = name
        self._territories = territories
        assert bonus > 0, "The continent bonus must be greater than 0"
        self._bonus = bonus
        
    @property
    def name(self):
        return self._name
    
    @property
    def territories(self):
        return self._territories
    
    @property
    def bonus(self):
        return self._bonus