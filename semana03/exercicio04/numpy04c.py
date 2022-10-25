from numpy.lib.stride_tricks import as_strided
import numpy as np

l = [1,2,3]
a = np.array([1,2,3])

a = np.sqrt(a)
b= np.log(a)
print(a)
print(b)