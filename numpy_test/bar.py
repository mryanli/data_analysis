import numpy as np
import matplotlib.pyplot as mp
n = 12
x = np.arange(n)
y1 = (1-x/n)*np.random.uniform(0.5,1.0,n)
y2 = (1-x/n)*np.random.uniform(0.5,1.0,n)
mp.ylim(-1.2,1.2)
mp.xticks(x,x+1)
mp.grid(axis = 'y',linestyle=':',color='black')
for _x,_y in zip(x,y1):
    mp.text(_x,_y,'%.2f'%_y,ha='center',va= 'bottom')
for _x, _y in zip(x, -y2):
    mp.text(_x, _y, '%.2f' % _y, ha='center', va='top')
mp.bar(x,y1)
mp.bar(x,-y2)

mp.show()