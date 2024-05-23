import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.animation import FuncAnimation

years = np.array([2000, 2002, 2005, 2007, 2010]).reshape(-1, 1)
percentage = np.array([6.5, 7.0, 7.4, 8.2, 9.0])

fig, ax = plt.subplots()
ax.set_xlim(1995, 2015)
ax.set_ylim(0, 10)
ax.set_xlabel('Rok')
ax.set_ylabel('Procent bezrobotnych')

scatter = ax.scatter(years, percentage, color='blue')
line, = ax.plot([], [], color='red', lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(1995, 2015, 100)
    y = model.coef_ * x + model.intercept_
    line.set_data(x, y)
    return line,

model = LinearRegression()
model.fit(years, percentage)
ani = FuncAnimation(fig, animate, frames=100, init_func=init, blit=True)
plt.show()
