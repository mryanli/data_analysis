import numpy as np
import matplotlib.pyplot as mp

n = 1000
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
d = np.sqrt(x**2+y**2)
mp.xlabel('x')
mp.ylabel('y')
mp.tick_params(labelsize=30)
# mp.grid(linestyle=':')
mp.scatter(x,y,s=30,c=d,cmap='jet_r',alpha=0.5,
           marker = '*')
mp.show()