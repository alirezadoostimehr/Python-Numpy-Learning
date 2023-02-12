# Write a NumPy program to create an element-wise comparison
# (greater, greater_equal, less and less_equal) of two given arrays.

import numpy as np

arr1 = np.array([0, 2, 3, 4])
arr2 = np.array([1, 2, 3, np.inf])

print("First Array: ", arr1)
print("Second Array: ", arr2)

print("Less: ", np.less(arr1, arr2))
print("Less equal: ", np.less_equal(arr1, arr2))
print("Equal: ", np.equal(arr1, arr2))
print("Greater: ", np.greater(arr1, arr2))
print("Greater equal:", np.greater_equal(arr1, arr2))
