class ToroidalPosition:
    """
    Descriptor for position (x, y) on a toroidal integer grid.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._name = None
    
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, name):
        if instance is None:
            return self
        return instance.__dict__[self._name]
    
    def __set__(self, instance, value):
        x, y = value
        instance.__dict__[self._name] = (x%self.width, y%self.height)
    
    @classmethod
    def from_model(cls, model):
        return cls(width=model.width, height=model.height)
    
