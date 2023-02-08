# Write a NumPy program to test whether none of
# the elements of a given array is zero.

import numpy as np

arr_no_zeros = np.array([[1, 2], [3, 4]])
arr_with_zero = np.array([[1, 0], [3, 4]])

print("With Builtin Function:")
print("Answer for no zeros:", np.all(arr_no_zeros))
print("Answer for with zero:", np.all(arr_with_zero))

print("Without Builtin Function:")
print("Answer for no zeros:", end=" ")
printed = False
for i in np.nditer(arr_no_zeros):
    if (i == 0):
        print("False")
        printed = True
        break
if (not printed):
    print("True")

print("Answer for with zero:", end=" ")
printed = False
for i in np.nditer(arr_with_zero):
    if (i == 0):
        print("False")
        printed = True
        break
if (not printed):
    print("True")