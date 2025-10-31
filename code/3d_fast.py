import matplotlib.pyplot as plt
import numpy as np

N = 10000
NN = 100
x = np.random.randint(-1, 2, size=N)
y = np.random.randint(-1, 2, size=N)
z = np.random.randint(-1, 2, size=N)

for i in range(NN):
    x = np.append(x, np.random.randint(-1, 2, size=N)) 
    y = np.append(y, np.random.randint(-1, 2, size=N))
    z = np.append(z, np.random.randint(-1, 2, size=N))

    plt.plot(np.cumsum(x), np.cumsum(y), np.cumsum(z))
    plt.pause(0.05)
