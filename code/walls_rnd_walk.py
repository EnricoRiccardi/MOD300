import numpy as np
import matplotlib.pyplot as plt


box = 50
N = 100000
position = [0]
for i in range(N):
    step = np.random.randint(-1, 2)
    new_pos = position[-1]+step
    if new_pos > box/2:
        new_pos -= 1
    if new_pos < -box/2:
        new_pos += 1

    position.append(new_pos)
    
    plt.plot(position, color='r')
    plt.pause(0.05)
