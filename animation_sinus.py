import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2*np.pi, 200)
fig, ax = plt.subplots()
line1, = ax.plot(x, np.sin(x))
line2, = ax.plot(x, np.cos(x))

def update(frame):
    y1 = np.sin(x + 0.1*frame)
    y2 = np.cos(x + 0.1*frame)
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    return (line1, line2)

ani = FuncAnimation(fig, update, 
                    frames = 100, 
                    interval=50, 
                    blit = True)
plt.show()