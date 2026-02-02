from agent import Agent
import random
class Prey(Agent):
    def __init__(self, 
                 model, 
                 uid, 
                 position = None, 
                 energy: int = 10):
        super().__init__(model, uid, position)
        self.energy = energy

    def move(self):
        # TODO :
        # 1) Move (random 4-neighborhood)
        self.random_walk()

        #x, y = random.choice([
        #    (0, 1),  # op
         #   (0, -1), # ned
          #  (1, 0),  # højre
           # (-1, 0)  # venstre
        #])

        #new_position = (self.position[0] + x, self.position[1] + y)
        #if self.model.is_position_valid(new_position):
        #    self.position = new_position

        # 2) energy -= 1
        self.energy -= 1

        # 3) die if energy <=0
        if self.energy <= 0:
            self.model.remove_agent(self)



        #raise NotImplementedError
    
    def interact(self):
        pass

    def reproduce(self):


        # TODO :
        # If energy >= REPRODUCE_THRESHOLD:
        #       - (optional) at a certain possibility        
        #       - create a new Prey (baby) at same position (or neighbor)
        #       - call model.add_agent(baby) 
        #       - reduce parent's energy (e.g. energy //= 2)

        threshold = 40
        energy_cost = 15
        probability = 0.40
        if self.energy >= threshold and self.model.rng.random() < probability:
            new_uid = self.model.next_uid()
            self.model.set_uid += 1
            lamb = Prey(
                self.model,
                uid=new_uid,
                position=self.position,
                energy=energy_cost
            )
            self.model.add_agent(lamb)
            self.energy //= energy_cost

        #raise NotImplementedError