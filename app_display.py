import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt, animation
from matplotlib import colors 
from wolf_sheep_model import World

def run_app():
    model = World(200)

    fig, ax = plt.subplots()
    ax.set_xlim(0, model.world_size)
    ax.set_ylim(0, model.world_size)
    ax.set_aspect("equal")

    sheep_scatter = ax.scatter([], [], s=20, c="green")
    wolf_scatter  = ax.scatter([], [], s=40, c="red", marker="^")
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update(frame):
        model.step()

        sheep_pos = np.array([[s.x, s.y] for s in model.sheep])
        wolf_pos  = np.array([[w.x, w.y] for w in model.wolves])

        sheep_scatter.set_offsets(sheep_pos)
        wolf_scatter.set_offsets(wolf_pos)

        text.set_text(f"t={model.time}  Sheep={len(model.sheep)} Wolves={len(model.wolves)}")
        return sheep_scatter, wolf_scatter, text

    ani = animation.FuncAnimation(fig, 
                                  update, 
                                  interval=300, 
                                  blit=False, 
                                  cache_frame_data=False,
                                  )
    plt.show()


if __name__ == "__main__":
    run_app()


