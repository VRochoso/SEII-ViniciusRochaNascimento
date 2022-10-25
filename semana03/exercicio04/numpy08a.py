import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8]])
print(a)

b = a[0,1]
print(b)
b = a[0,:]
print(b)
b = a[0,1:3]
print(b)
b = a[:,0]
print(b)
b = a[-1,-1]
print(b)

a = np.array([[1,2],[3,4], [5,6]])
print(a)

bool_idx = a>2
print(bool_idx)
print(a[bool_idx])
print(a[a>2])
b = np.where(a>2,a,-1)
print(b)