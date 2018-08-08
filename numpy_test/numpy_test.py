# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import datetime
import numpy as np
from numpy import pi
from matplotlib import pyplot as mp
import matplotlib.gridspec as mg

gs =mg.GridSpec(3,3)
mp.subplot(gs[0:2,1:])
mp.text(
    0.5,0.5,'1',size = 36
)
mp.figure('正弦函数',figsize=(6,4),dpi=120)
mp.title(u'cos',fontsize=20)
mp.xlabel('x',fontsize = 12)
mp.ylabel('y',fontsize = 12)
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

x = np.linspace(-pi,pi,1000)
cos_y = np.cos(x) / 2
sin_y = np.sin(x)

mp.plot(x,cos_y,linestyle = ':',linewidth = 2,color = 'red',label='y=1\\2cos(x)')
mp.plot(x,sin_y,label='y = sin(x)')
mp.legend()
# mp.plot('v','r',data={'v':a,'r':b})
# mp.xlim(x.min()*1.1,x.max())
# mp.ylim(sin_y.min(),sin_y.max())

# mp.xticks(np.linspace())
mp.xticks([-pi,-pi/2,0,pi/2,pi],[r'$-\pi$',r'$-\frac{\pi}{2}$','0',r'$\frac{\pi}{2}$',r'$\pi$'])
mp.yticks([-1,-0.5,0,0.5,1])

mp.plot(np.array([pi/2 for i in range(15)]),np.linspace(0,1,15),linestyle='--')

mp.scatter(pi/2,1,edgecolor='red',facecolor='white',zorder=10)
mp.scatter(pi/2,0,edgecolor='red',facecolor='white',zorder=10)

xo = pi/2
yo_cos = np.cos(xo)
yo_sin = np.sin(xo)

mp.annotate(
    r'$\frac{1}{2}cos(\frac{3\pi}{4})=-\frac{\sqrt{2}}{4}$',
    xy = (xo,yo_cos),
    xycoords = 'data',
    xytext=(-90,-40),
    textcoords='offset points',
    arrowprops = dict(arrowstyle='->',
                      connectionstyle = 'arc3,rad=0.2')
)



ax = mp.gca()
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
ax.spines['top'].set_color(None)
ax.spines['right'].set_color(None)
mp.show()


print(1,23,)






