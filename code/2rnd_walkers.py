import numpy as np
import matplotlib.pyplot as plt


N=100000
distance=[0]
distance2=[0]
for i in range(N):
    step = np.random.randint(-1, 2)
    distance.append(distance[-1]+step)
    
    step = np.random.randint(-1, 2)
    distance2.append(distance2[-1]+step)

    plt.plot(distance, color='r')
    plt.plot(distance2, color='g')
    plt.pause(0.05)
