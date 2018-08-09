
import numpy as np
import matplotlib.pyplot as mp

mp.pie(
    [26,35,32,34,45],
    [0.05,0.01,0.01,0.01,0.01],
    ['Python','JavaScript','C++','C','PHP'],
    ['dodgerblue','orangered','limegreen','violet','gold'],
    '%d%%',shadow=True,startangle=0
)
mp.axis('equal')
mp.show()