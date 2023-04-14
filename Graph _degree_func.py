import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

plt.title("График функции y = x^(2) + 14 для сетки [-30; 30; 30]")

plt.xlabel("x")

plt.ylabel("y")

x = np.linspace(-30, 30, 30)

y = x**2 + 14

ax.plot(x, y)

plt.show()