import matplotlib.pyplot as plt
import numpy as np

N = 10000
NN = 100
x = 2*np.random.randint(0,2,size=N)-1
y = 2*np.random.randint(0,2,size=N)-1

for i in range(NN):
    x = np.append(x, 2*np.random.randint(0,2,size=N)-1) 
    y = np.append(y, 2*np.random.randint(0,2,size=N)-1) 
    plt.plot(np.cumsum(x),np.cumsum(y))
    plt.pause(0.05)
