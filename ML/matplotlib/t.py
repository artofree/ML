__author__ = 'guo'


import numpy as np
import matplotlib.pyplot as plt

intercept =np.random.random(1)
coef =np.random.random(2)
print(intercept ,coef)
lx =np.arange(0 ,12)
ly =(-lx *coef[0] +intercept) /coef[1]
print(lx)
print(ly)
plt.plot(lx ,ly ,c ='yellow')
plt.show()