
from abc import ABC, abstractmethod
import random

class Agent(ABC):

    """
    Abstract agent base class.
    subclasses MUST implement step().
    """
    def __init__(self, model, uid, position = None):
        self.model = model
        self.uid = uid
        self.position = position if position is not None else model.random_position()
        self.alive = True        

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]
    
    def die(self):
        self.alive = False

    def random_walk(self):
        """Von Neumann neighborhood random move using model RNG"""
        dx, dy = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
        x, y = self.position
        self.position = (x+dy, y+dy)


    @abstractmethod
    def move(self):
        raise NotImplementedError
    @abstractmethod
    def interact(self):
        raise NotImplementedError
    @abstractmethod
    def reproduce(self):
        raise NotImplementedError