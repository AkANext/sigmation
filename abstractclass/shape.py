from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @classmethod
    @abstractmethod
    def from_config(cls, config):
        
        pass

    @staticmethod
    @abstractmethod
    def validate_config(config):
        """
        Validate input configuration
        """
        pass
    

    def __str__(self):
        return f"I am a {self.__class__.__name__} shape with area {self.area()}"


config_dic = {'width':5, 'height':4}

class Rectangle(Shape):

    def __init__(self, **kwarg):
        self.width = kwarg['width']
        self.height = kwarg['height']
    def area(self):
        return self.width*self.height



class Circle(Shape):
    pass

r = Rectangle(**config_dic)
print(r)