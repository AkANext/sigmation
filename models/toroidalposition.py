class ToroidalPosition:
    """
    Descriptor for a 2D toroidal world.
    - position is (x,y)
    - x is wrapped in range [0, width-1] 
    - y is wrapped in range [0, height-1]
    """

    def __init__(self, width: int, height: int):
        if not type(width)==int or type(height)==int:
            raise TypeError("width and height must be integers!")
        
        if width <=0 or height <=0:
            raise ValueError("width and height must be positive!")
        
        self.width = width
        self.height = height
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name
    
    def __get__(self, instance, value):
        x = x%self.width
        y = y%self.height

        instance.__dict__[self._name] = (x,y)
    
    @classmethod
    def from_world(cls, width: int, height:int):
        """        
        :param width: width of the world
        :type width: int
        :param height: height of the world
        :type height: int
        """
        return cls(width=width, height=height)