import numpy as np
import matplotlib.pyplot as plt


N=100000
x = [0]
y = [0]
for i in range(N):
    step = np.random.randint(-1, 2)
    x.append(x[-1]+step)
    
    step = np.random.randint(-1, 2)
    y.append(y[-1]+step)

    plt.plot(x, y, color='r')
    plt.pause(0.05)
