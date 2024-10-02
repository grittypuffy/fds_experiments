"""
Write a Numpy program that uses the np.sqrt ufunc to compute the square root of each
element in a 2D NumPy array.
"""
import numpy as np

def sqrt_ufunc():
    array = [4, 81, 16, 25, 36, 100]
    print("Original array: ", array)
    print(f"Square root array: {np.sqrt(array)}")