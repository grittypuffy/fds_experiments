"""
Write a Numpy program that creates a custom ufunc that adds 10 to every element in
a Numpy array. Use this ufunc on a 1D array of integers.
"""
import numpy as np

def add_ten(x):
    return x + 10

def add_ten_ufunc():
    add_ten_ufunc = np.frompyfunc(add_ten, 1, 1)

    # Creating a 1D array of integers
    arr = np.array([1, 2, 3, 4, 5])

    # Applying the custom ufunc
    result = add_ten_ufunc(arr)

    print("Add 10 with ufunc:", result)