
from model import Model
from prey import Prey
from predator import Predator
from toroidalposition import ToroidalPosition

def make_toroidal_classes(model):
    class ToroidalPrey(Prey):
        position = ToroidalPosition.from_model(model)

    class ToroidalPredator(Predator):
        position = ToroidalPosition.from_model(model)


    return ToroidalPrey, ToroidalPredator

if __name__ == "__main__":
    model = Model(width=10, height=6, seed=2)
    ToroidalPrey, ToroidalPredator = make_toroidal_classes(model)

    for _ in range(12):
        model.add_agent(ToroidalPrey(model, uid=model.next_uid))
    for _ in range(4):
        model.add_agent(ToroidalPredator(model, uid=model.next_uid))

    for _ in range(30):
        prey_count = sum(isinstance(a, ToroidalPrey) for a in model.agents)
        pred_count = sum(isinstance(a, ToroidalPredator) for a in model.agents)
        print(f"t={model.time}, sheep = {prey_count}, wolf = {pred_count}")
        model.step()