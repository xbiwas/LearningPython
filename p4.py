import numpy as np

a = np.array([1,2,3], dtype='int32')
b = np.array([4,3,2])
x = np.array([[1,2,3,4],[5,6,7,8]])

print(a * b)

# Get Dimension
print(a.ndim)
print(b.ndim)

# Get shape
print(a.shape)
print(b.shape)

# Get Data type
print(a.dtype)
print(b.dtype)

# Get sizef
print(a.itemsize)
print(b.itemsize)

print(x)