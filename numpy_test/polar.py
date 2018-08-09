import numpy as np
import matplotlib.pyplot as mp

t = np.linspace(0,2*np.pi,1000)
r_rose = 5 * np.sin(2*t)
r = 0.8*t
ax = mp.gca(projection='polar')
ax.set_xlabel('x')
ax.set_ylabel('y')
mp.title('3D')
n = 1000

mp.plot(t,r)
mp.plot(t,r_rose)

mp.grid(linestyle=':')


mp.show()