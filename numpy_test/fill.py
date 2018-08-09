import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-2,2,200)
y1 = x**2
y2 = x + 1
mp.grid(linestyle=':')
mp.title('FILL')
mp.plot(x,y1,label=r'$y = x^2$')
mp.plot(x,y2,label = r'$y = x + 1$')
mp.fill_between(x,y1,y2,y2>y1,color='red',alpha=0.1)
mp.legend()
mp.show()