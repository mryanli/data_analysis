import  numpy as np

a  = np.arange(1,10).reshape(3,3)

np.savetxt('text.csv',a,delimiter=',',fmt='%d')
