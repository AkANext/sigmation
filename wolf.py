
import random
import numpy as np
from models.agents import Agent

class Wolf(Agent):

    def __init__(self, 
                 model,
                 position=None, 
                 energy = 12,
                 p_reproduce = 0.05, 
                 energy_loss = 1,
                 energy_gain_from_food = 8,
                 repro_energy_threshold = 18
                 ):
        super().__init__(model, position)
        self.p_reproduce = p_reproduce
        self.energy = energy
        self.energy_loss = energy_loss
        self.energy_gain_from_food = energy_gain_from_food
        self.repro_energy_threshold = repro_energy_threshold


   
    
    def feed(self,model):
        """If possible, eat a sheep at nearby."""

    def spawn_offspring(self):
        
        if self.energy >= self.repro_energy_threshold:
            if self.model.rng.random()<self.p_reproduce:
                self.model.add_agent(self.__class__(self.model, 
                                                    position = None,
                                                    p_reproduce = self.p_reproduce,
                                                    energy = 12,
                                                    energy_loss = self.energy_loss,
                                                    energy_gain_from_food = self.energy_gain_from_food,
                                                    repro_energy_threshold = self.repro_energy_threshold
                                                    ))

    def step(self):
        
        self.move()         
        self.feed()
        self.spawn_offspring()
        # Handle death and reproduction
        if self.energy < 0:
            self.alive = False