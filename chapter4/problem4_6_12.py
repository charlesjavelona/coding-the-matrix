import numpy as np

def is_triangular(matrix):
    """
    Input: A matrix that may or may not be triangular
    Output: Boolean whether the matrix is a triangular or not. True if it is. False if it's not.

    What is a triangular matrix ? What are the structure ?
    Below are two triangular matrix. The first is an upper triangular. The other is a lower tringular 
    
    [1, 1, 1, 1]
    [0, 1, 1, 1]
    [0, 0, 1, 1]
    [0, 0, 0, 1]

    [1, 1, 1, 1]
    [1, 1, 1, 0]
    [1, 1, 0, 0]
    [1, 0, 0, 0]

    Computationally, how does one know if it's a triangular ?

    An upper triangular matrix has the following characteristics
    - It is a square matrix
    - Below the diagonal matrix are 0's

    A lower triangular matrix has the following characteristics
    - It is a square matrix
    - Above the diagonal matrix are 0's
    """
    assert matrix.shape[0] == matrix.shape[1]
    assert type(matrix) == type(np.array([]))
    is_upper = False
    is_lower = False

    if(is_upper_triangle(matrix)):
        is_upper = True
    if(is_lower_triangle(matrix)):
        is_lower = True 

    return True if(is_upper or is_lower) else False

def is_upper_triangle(arr: np.array([])) -> np.array([]):
    """
    Input: arr is a matrix. That has all 1's rown and column.
    Output: return a boolean if the matrix is an upper triangle.

    Ex: 
    [1, 1, 1]
    [1, 1, 1]
    [1, 1, 1] 

    [1, 1, 1]
    [0, 1, 1]
    [0, 0, 1]

    """
    for r in range(1, len(arr)):
        for c in range(0, r):
            if(arr[r][c] != 0):
                return False
    return True 
                


def is_lower_triangle(arr: np.array([])) -> np.array([]):

    """
    https://stackoverflow.com/questions/17395367/python-how-can-i-find-the-square-matrix-of-a-lower-triangular-numpy-matrix-w
    Input: arr is a matrix. That has all 1's rown and column.
    Output: return a boolean if the matrix is lower triangular 

    Ex: 
    [1, 1, 1]
    [1, 1, 1]
    [1, 1, 1] 

    [1, 0, 0]
    [1, 1, 0]
    [1, 1, 1]
    """
    #Asser that arr is a square matrix
    assert arr.shape[0] == arr.shape[1]
    assert type(arr) == type(np.array([]))
    for r in range(len(arr)):
        for c in range(r+1, len(arr)):
            if(arr[r][c] != 0):
                return False
    return True 
