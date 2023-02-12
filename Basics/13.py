# Write a NumPy program to create an
# array of 10 zeros,10 ones, 10 fives.

import numpy as np

arr1 = np.zeros(10)
print("10 zeros: ", arr1)

arr2 = np.ones(10)
print("10 ones(method 1): ", arr2)

arr3 = arr1 + 1
print("10 ones(method 2): ", arr3)

arr4 = np.ones(10)*5
print("10 fives: ", arr4)
