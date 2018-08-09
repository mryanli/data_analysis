import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000
ax = mp.gca(projection='3d')
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
z = np.random.normal(0,1,n)

d = np.sqrt(x**2+y**2+z**2)
ax.scatter(x,y,z,c=d,cmap='jet_r',marker='*')

mp.show()