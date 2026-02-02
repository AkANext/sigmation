import random


class MyWorld:
    width: int
    height: int
    seed: int|None=None

    def __init__(self):
        self.rng = random.Random(self.seed)
        self.agents = []
        self.step_count = 0

        # for statistic
        self.prey_history = []
        self.pred_history = []
    
    def random_position(self):
        return (self.rng.randrange(self.width), self.rng.randrange(self.height))
    
    def add_agent(self, agent):
        self.agents.append(agent)

    def step(self):
        self.step_count += 1

        # Shuffle list of agents for randomness
        self.rng.shuffle(self.agents)
        for a in self.agents:
            if a.alive:
                a.step()

        # Remove dead agents
        self.agents = [a for a in self.agents if a.alive]