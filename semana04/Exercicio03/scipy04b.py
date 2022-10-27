import numpy as np
import matplotlib.pylot as plt
import scipy as sp
from scipy.optimize import curve_fit
from scipy.interpolate import interpld

t_data = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
y_data = np.random.randn[0:30]

plt.plot(t_data,y_data, 'o--')

def func(x, A, w, phi):
    return A*np.cos(w*x+phi)
print(w)

popt, pcov = curve_fit(func, t_data, y_data, p0=(4, np.pi,0))
print(popt)
print(pcov)
print(np.diag(pcov))
print(np.sqrt(np.diag(pcov)))

t = np.linspace(0,10,100)
y = func(t,A,w,phi)

plt.scatter(t_data, y_data)
plt.plot(t,y)