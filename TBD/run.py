from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
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

    prey_start = 40
    for _ in range(prey_start):
        model.add_agent(ToroidalPrey(model, uid=model.next_uid))

    pred_start = 10
    for _ in range(pred_start):
        model.add_agent(ToroidalPredator(model, uid=model.next_uid))

    time_steps = []
    prey_counts = []
    pred_counts = []

    model_time = 160
    for _ in range(model_time):
        prey_count = sum(isinstance(a, ToroidalPrey) for a in model.agents)
        pred_count = sum(isinstance(a, ToroidalPredator) for a in model.agents)

        time_steps.append(model.time)
        prey_counts.append(prey_count)
        pred_counts.append(pred_count)

        print(f"t={model.time}, sheep = {prey_count}, wolf = {pred_count}")

        model.step()

    # scatterplot med funcanimation

    fig, ax = plt.subplots()
    def update(frame):
        x = np.array(time_steps[:frame])
        y_prey = np.array(prey_counts[:frame])
        y_pred = np.array(pred_counts[:frame])

        data_pred = np.stack([x, y_pred]).T
        scat_pred.set_offsets(data_pred)

        data_prey = np.stack([x, y_prey]).T
        scat_prey.set_offsets(data_prey)

        return scat_pred, scat_prey

    scat_pred = ax.scatter([], [], color='red', s=5, label='Predators')
    scat_prey = ax.scatter([], [], color='blue', s=5, label='Prey')

    ax.set_title('Predator/Prey Population Over Time')
    ax.set(xlim=[0, model_time], ylim=[0, prey_start + 40], xlabel='Time [T]', ylabel='population')
    ax.legend()
    ani = FuncAnimation(fig, update, frames=len(time_steps), interval=50, blit=True)
    plt.show()









