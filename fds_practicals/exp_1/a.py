# Write a Numpy program to perform the basic arithmetic operation

import numpy as np

def numpy_operations():
    array_1 = np.array([1, 2, 3, 4, 5, 6], 'i')
    array_2 = np.array([10, 11, 12, 13, 14, 15], 'i')
    print("Array 1:", array_1, "\nArray 2:", array_2)
    print("Add:", np.add(array_1, array_2))
    print("Sub:", np.subtract(array_1, array_2))
    print("Multiply:", np.multiply(array_1, array_2))
    print("Divide:", np.divide(array_1, array_2))
    print("Mod:", np.mod(array_1, array_2))
    print("Power:", np.power(array_1, array_2))