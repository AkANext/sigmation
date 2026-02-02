import random
import numpy as np
from abc import ABC, abstractmethod
from model import Model


class Agent(ABC):
    """The base agent class"""
    def __init__(self, 
                 model: Model,
                 position: list[int, int],
                 speed: float):
        """Initialize an agent.
        Args:
            energy: Starting amount of energy
            p_reproduce: Probability of reproduction
            cell: Cell in which the animal starts 
        """
        self.model = model 
        self.alive = True
        self.position = position
        self.speed = speed
    
    def move(self):
        """
        Random walk 
        """        
        angle = random.random()*2*np.pi
        delta_x = np.cos(angle)*self.speed
        delta_y = np.sin(angle)*self.speed
        self.x = self.x + delta_x
        self.y = self.y + delta_y


    @abstractmethod
    def feed(self):
        pass
    
    @abstractmethod
    def spawn_offspring(self):
        """Create offspring by splitting energy and creating new instance.
        self.energy /=2

        return self.__class__(self.x+random.uniform(-5,5),
                            self.y+random.uniform(-5, 5),
                            self.speed,
                            self.world_size
                            )
        """
        pass
                        
    @abstractmethod
    def step(self):
        """Execute one step of the animal's behavior."""
        pass

