import numpy as np
import matplotlib.pyplot as plt


N=100000
distance=[0]
for i in range(N):
    step = np.random.randint(-1, 2)
    distance.append(distance[-1]+step)
    
    plt.plot(distance, color='r')
    plt.pause(0.05)
