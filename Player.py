class Player:
    
    def __init__(self, name):
        assert isinstance(name, str)
        self._name = name
        self._cards = ()
        
    @property
    def name(self):
        return self._name