import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

plt.title("График функции y = sin(2x + 4) + 4 для сетки [-30; 30; 30]")

plt.xlabel("x")

plt.ylabel("y")

x = np.linspace(-30, 30, 30)

y = np.sin(2*x + 4) + 4

ax.plot(x, y)

plt.show()