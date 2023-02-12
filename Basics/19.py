# Write a NumPy program to create a vector
# with values ranging from 15 to 55 and
# print all values except the first and last.

import numpy as np

arr = np.arange(15, 56)
print(arr[1:-1:])