import numpy as np
import copy
import random
import math
from models.model import Model
from sheep import Sheep 
from wolf import Wolf


class World(Model): 
    """Wolf-sheep Predation Model.
    A model for simulating wolf and sheep (predator-prey) ecosystem modelling.
    """

    def __init__(
        self,
        world_size,
        n_sheep=50,
        n_wolves=4,
        sheep_reproduce=0.19,
        wolf_reproduce=0.05,
        wolf_gain_from_food=8,
    ):
        """Create a wolf-Sheep model with the given parameters.

        Args:
            n_sheep: Number of sheep to start with
            n_wolves: Number of wolves to start with
            sheep_reproduce: Probability of each sheep reproducing each step
            wolf_reproduce: probability of each wolf reproducing each step
            wolf_gain_from_food: Energy a wolf gains from eating a sheep
        """
        super().__init__(world_size)
        self.time = 0
        self.sheep = []
        self.wolves = []
        self.new_sheep = []
        self.new_wolves = []
        self.sheep_to_remove = []
        self.wolves_to_remove = []


        # Populate world
                
        for _ in range(n_sheep):
            x, y = np.random.uniform(0, self.world_size, 2)
            self.sheep.append(Sheep(x,y,
                                    self.world_size,
                                    p_reproduce=0.16,
                                    speed=20,
                                    energy_loss=1.5))
        

        for _ in range(n_wolves):
            x, y = np.random.uniform(0, self.world_size, 2)
            self.wolves.append(Wolf(x,y,
                                    self.world_size,
                                    p_reproduce=0.055,
                                    energy = 25,
                                    energy_loss = 6,
                                    energy_gain_from_food=8))


        self.sheep_reproduce = sheep_reproduce
        self.wolf_reproduce = wolf_reproduce
        self.wolf_gain_from_food = wolf_gain_from_food


    def setup(self):
        # Add newborns, remove the dead
        pass

    def step(self):
        """
        Add newborns, remove the dead,

        """
        for s in self.sheep:
            if not s.alive:
                self.sheep.remove(s)
                del s
        for w in self.wolves:
            if not w.alive:
                self.wolves.remove(w)
                del w

        self.sheep.extend(self.new_sheep)
        self.wolves.extend(self.new_wolves)

        self.new_sheep = []
        self.new_wolves = []
                
        for s in self.sheep:
            s.step(self)

        for w in self.wolves:
            w.step(self)
        
        self.time += 1