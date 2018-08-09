import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

ax = mp.gca(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
mp.title('3D')
n = 1000
x,y = np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
z = (1- x/2 + x**5 + y **3)* np.exp(-x**2 - y**2)

#3D曲面
# ax.plot_surface(x,y,z,rstride = 40,cstride = 40,linewidth=0.5,color='orangered',
#                 cmap='jet')
#3D曲线
ax.plot_wireframe(x,y,z,rstride = 40,cstride = 40,linewidth=0.5,color='orangered',
                cmap='jet')

mp.show()