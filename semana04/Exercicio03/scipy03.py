import numpy as np
import matplotlib.pylot as plt
import scipy as sp
from scipy.optimize import minimize
from scipy.interpolate import interpld

x = np.linspace(0,10,10)
y = x**2 * np.sin(x)
plt.scatter(x,y)

f = interpld(x,y, kind='linear')
x_dense = np.linspace(0,10,100)
y_dense = f(x_dense)
plt.plot(x_dense, y_dense)

f = interpld(x,y, kind='cubic')
x_dense = np.linspace(0,10,100)
y_dense = f(x_dense)
plt.plot(x_dense, y_dense)