#
# Numpy gives you an enormous range of fast and efficient ways of creating arrays and
# manipulating numerical data insde them. While a Python list can contain different data types
# within a single list, all of the elements in a Numpy array should be homogeneous. 
# The mathmatical operations that are menat to be performed on arrays would be extremely
# inefficient if the arrays weren't homogeneous.
#

import numpy as np

def main():
    # Create 1D array
    a = np.array([[1,2,3],
                 [4,5,6]])
    print(a, a[0], type(a))

    # Create an array filled with 0's
    a = np.zeros(2)
    print(a, len(a))

    # Create an array filled with 1's
    a = np.ones(2)
    print(a, len(a))

    # Create an empy array. The function empty creates an array whose initial content is
    # random and depends on the state of the memory. The reason to use empty over zeros
    # (or something similar) is speed - just make sure to fill every element afterwards
    a = np.empty(2)
    print(a, len(a))

    # Create and array with range of elements
    a = np.arange(4)
    print(a, len(a))

    # Create an array with values that are spaced linearly in a specified interval
    a = np.linspace(0, 10, num=5)
    print(a, len(a))

    # Specifying data type while the default data type is floating point (np.float64)
    # User can explicitly specify which data type we want using the dtype keyword
    a = np.ones(2, dtype=np.int64)
    print(a, len(a))

    # Sorting elements
    arr = np.array([2,6,5,2,1,3,4,5,6,1])
    arr = np.sort(arr)
    print(arr)

    # Concatenate arrays
    x = np.array([1,2,3,4])
    y = np.array([5,6,7,8])
    print(np.concatenate((x, y), axis=0))

    # array shape, size, dimensions
    arr = np.array([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12]])
    print(arr.ndim, arr.size, arr.shape)

    # reshape array
    arr = np.array([1,2,3,4,5,6])
    arr = arr.reshape(2,3)
    print(arr)

if __name__ == '__main__':
    main()