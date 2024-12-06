import numpy as np
# core library for scientific computation
array = np.array([1,2,3], [4,5,6])
print(array)
print(type(array))
print(array.shape)

array = np.zeros((3,4), dtype=int)
array = np.ones((3,4), dtype = int)
array = np.full((3,4), 5, dtype = int)
array = np.random.random((3,4))

print(array)
print(array[0,0])
print(array > 0.2)
print(array[array > 0.2])
print(np.round(array))

dimensions_inch = [1,2,3]
dimensions_cm = [x * 2.54 for x in dimensions_inch]