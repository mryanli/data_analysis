import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0.1,5,100)
y = np.log(x)

ax = mp.gca()
ax.spines['bottom'].set_position(('data',0))

mp.semilogy(y)

mp.show()