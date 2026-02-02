import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
fig, ax = plt.subplots()
ax.set_xlim([0,10])
ax.set_ylim([-2,2])
scat = ax.scatter(x[0], y[0])

def update(frame):
    # update the scatter plot:
    tx = x[:frame]
    ty = y[:frame]
    data = np.stack([tx, ty]).T
    scat.set_offsets(data)
    # update the line plot:
    return (scat, )





ani = FuncAnimation(fig=fig, func=update, frames=len(x)-1, 
                    interval=30)
plt.show()