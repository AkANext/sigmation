from agent import Agent
import random
from prey import Prey


class Predator(Agent):

    def __init__(self,
                 model,
                 uid,
                 position=None,
                 energy: int = 15):
        super().__init__(model, uid, position)
        self.energy = energy

    def move(self) -> None:
        # TODO :
        # - move randomly
        self.random_walk()
        # - energy -= 1
        self.energy -= 1
        # - if energy <= 0: die()
        if self.energy <= 0:
            self.die()

        # raise NotImplementedError

    def interact(self) -> None:
        # TODO :
        # - find prey on same cell and eat ONE:
        # - mark eaten prey dead (prey.die())
        # - gain energy
        agents_here = self.model.agents_at(self.position)
        prey_here = [a for a in agents_here if isinstance(a, Prey)]
        if prey_here:
            prey_eaten = random.choice(prey_here)
            prey_eaten.die()
            self.energy += prey_eaten.energy

        # raise NotImplementedError

    def reproduce(self) -> None:
        # TODO (Lesson 2) optional:
        # - if energy >= threshold (and at a certain possibility):
        #     spawn new Predator, reduce energy
        threshold = 70
        energy_cost = 25
        probability = 0.2
        if self.energy >= threshold and self.model.rng.random() < probability:
            new_uid = self.model.next_uid()
            self.model.set_uid += 1
            cub = Predator(
                self.model,
                uid=new_uid,
                position=self.position,
                energy=energy_cost
            )
            self.model.add_agent(cub)
            self.energy //= energy_cost
        # raise NotImplementedError