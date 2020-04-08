
from numpy import random as rng
import matplotlib.pyplot as plt
import numpy as np
num_steps = 1000
x_final = []
y_final = []
displacement = []

def rand():
    x = 0
    num = []
    for i in range(num_steps):
        v = rng.random()
        if v <= 0.5:
            x = x - 1
        if v > 0.5:
            x = x + 1
        num.append(x)
    return num
    



for i in range(4):
    plt.subplot(2,2,i+1)
    plt.plot(rand(),rand())
    plt.axis(xmin = -30, xmax = 30, ymin = -30, ymax = 30)
plt.show()
plt.close()

for i in range(1000):
    x = rand()
    y = rand()
    x_final.append(x[-1])
    y_final.append(y[-1])
    displacement.append(np.sqrt((x[-1])**2 + (y[-1]**2)))
#print(displacement)
    
plt.scatter(x_final,y_final)
plt.show()
plt.close()
plt.scatter(np.arange(0,len(displacement)), displacement)
