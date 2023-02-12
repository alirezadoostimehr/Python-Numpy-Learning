# Write a NumPy program to test a given array element-wise
# for finiteness (not infinity or not a Number).

import numpy as np

arrayNoInfinit = np.array([0, 2, 3, 4])
arrayWithPositiveInfinit = np.array([1, 2, 3, np.inf])
arrayWithNegativeInfinit = np.array([1, 2, 3, np.NINF])
arrayWithInifint = np.array([1, 2, np.inf, np.NINF])

print("Answer for no infinit:", np.any(np.isinf(arrayNoInfinit)))
print("Answer for positive infinit:", np.any(np.isinf(arrayWithPositiveInfinit)))
print("Answer for negative infinit:", np.any(np.isinf(arrayWithNegativeInfinit)))
print("Answer for both infinit:", np.any(np.isinf(arrayWithInifint)))


