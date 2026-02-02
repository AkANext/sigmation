import random
import numpy as np
from models.agents import Agent


class Sheep(Agent):
    def __init__(self,
                 model,
                 position=None, 
                 speed = 25,
                 p_reproduce:float = 0.05, 
                 ):
        super().__init__(model, position)
        self.p_reproduce = p_reproduce
        self.speed = speed
    
    def spawn_offspring(self):
        if self.model.rng.random() < self.p_reproduce:
            self.model.add_agent(self.__class__(self.model, 
                                                position=self.position,
                                                p_reproduce=self.p_reproduce
                                                )
                                )

    def step(self):
        # Random walk
        self.move()
        # Reproduction
        self.spawn_offspring
        
    

    

         






