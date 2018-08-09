import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

mp.figure('annimatation')
mp.grid(linestyle=":")
mp.ylim(-3,3)
mp.xlim(0,20)

pl = mp.plot([],[],c = 'orangered')[0]
pl.set_data([],[])

def update(data):
    t,v = data
    x,y=pl.get_data()
    x.append(t)
    y.append(v)
    if t > 10:
        mp.xlim(t-10,t+10)
    pl.set_data(x,y)

def generator():
    t  = 0
    while 1:
        v = np.sin(2 * np.pi * t)*np.exp(np.sin(0.2*np.pi*t))
        yield t,v
        t += 0.05

anim = ma.FuncAnimation(mp.gcf(),update,generator,interval=30)





mp.show()

