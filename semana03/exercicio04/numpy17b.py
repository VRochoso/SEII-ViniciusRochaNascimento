import numpy as np

a = np.array([[1,1], [1.5,4.0]])
b = np.array([2200,5050])

x = np.linalg.inv(a).dot(b)
print(x)

x = np.linalg.solve(a,b)
print(x)