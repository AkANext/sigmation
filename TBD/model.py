import random


class Model:
    def __init__(self, width, height, seed=None):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive!")
        self.width = width
        self.height = height
        self.rng = random.Random(seed)
        self.agents = []
        self.time = 0
        self._next_uid = 0

    def random_position(self):
        return (self.rng.randrange(self.width), self.rng.randrange(self.height))

    def add_agent(self, agent):
        self.agents.append(agent)

    def remove_agent(self, agent):
        self.agents.remove(agent)

    def agents_at(self, pos):
        """
        TODO:
        return a list of agents who is occuppying the given position.
        """
        return [agent for agent in self.agents if agent.position == pos and agent.alive]

    def next_uid(self):
        uid = self._next_uid
        self._next_uid += 1
        return uid

    def step(self):
        """
        Random sequence for fairness
        """

        self.rng.shuffle(self.agents)

        # tod0:
        # - all agents Move
        # - all interact (eat)
        # - all reproduce (if possible)
        for agent in self.agents:
            if agent.alive:
                agent.move()
                agent.interact()
                agent.reproduce()

        # - model cleanup the DEAD, remove dead agent from the agent list
        self.agents = [agent for agent in self.agents if agent.alive]

        self.time += 1

    def run(self, steps: int):
        for _ in range(steps):
            self.step()
