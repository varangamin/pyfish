class Territory:
    
    def __init__(self, name, neighbors, owner, armies):
        assert isinstance(name, str)
        self._name = name
        self._owner = owner
        self._neighbors = neighbors
        assert armies > 0, "A territory must have at least 1 army"
        self._armies = armies
        
    @property
    def name(self):
        return self._name
    
    @property
    def neighbors(self):
        return self._neighbors
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        self._owner = owner
    
    @property
    def armies(self):
        return self._armies
    
    @armies.setter
    def armies(self, armies):
        assert armies > 0, "A territory must have at least 1 army"
        self._armies = armies