"""
Write a Numpy program that uses the np.where ufunc to create a new array from two
existing arrays based on a condition applied to a third array
"""
import numpy as np

def condition_numpy():
    array_1 = np.array([10, 20, 30, 40, 50])
    array_2 = np.array([1, 2, 3, 4, 5])
    condition_array = np.array([True, False, True, False, True])

    result_array = np.where(condition_array, array_1, array_2)

    print("Array 1:", array_1)
    print("Array 2:", array_2)
    print("Condition array:", condition_array)
    print("Resulting array:", result_array)