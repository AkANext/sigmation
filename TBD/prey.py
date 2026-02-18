from agent import Agent
import random


class Prey(Agent):
    def __init__(self,
                 model,
                 uid,
                 position=None,
                 energy: int = 10):
        super().__init__(model, uid, position)
        self.energy = energy

    def move(self):
        # TODO :
        # 1) Move (random 4-neighborhood)
        self.random_walk()
        # new_position = (self.position[0] + x, self.position[1] + y)
        # if self.model.is_position_valid(new_position):
        #    self.position = new_position
        # 2) energy -= 1
        self.energy -= 1
        # 3) die if energy <=0
        if self.energy <= 0:
            self.model.remove_agent(self)

        # raise NotImplementedError

    def interact(self):
        pass

    def reproduce(self):
        # 2TODO :
        # If energy >= REPRODUCE_THRESHOLD:
        #       - (optional) at a certain possibility
        #       - create a new Prey (baby) at same position (or neighbor)
        #       - call model.add_agent(baby)
        #       - reduce parent's energy (e.g. energy //= 2)

        if self.energy >= 20:
            if self.model.rng.random() < 0.3:
                lamb = self.__class__(
                    model=self.model,
                    uid=self.model.next_uid,
                    position=self.position,
                    energy=self.energy // 2
                )
                self.model.add_agent(lamb)
                self.energy //= 2

        # raise NotImplementedError