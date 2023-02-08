# Write a NumPy program to test whether any
# of the elements of a given array is non-zero.

import numpy as np

arr_no_zeros = np.array([[1, 2], [3, 4]])
arr_with_zero = np.array([[1, 0], [3, 4]])
arr_all_zeros = np.array([[0, 0], [0, 0]])

print("Answer for no zeros:", not np.all(arr_no_zeros!=0))
print("Answer for with zero:", not np.all(arr_with_zero!=0))
print("Answer for all zeros:", not np.all(arr_all_zeros!=0))