"""
Let a, b be real. Consider the equation z = ax + by. 
Prove that there are two 3 vectors v1, v2 such that the set of points [x, y, z] satisfying the equation is exactly the set of linear combination of v1 and v2. 
Hint. Specify the vectors using formulas involving a, b.


A linear combination is given a set V containing vectors of n length ([v1], [v2]). In this case, v1 and v2 contains 3 vectors [x, y, z]. 
a and b are scalars of V. Let v1 and v2 be x and y. So ax + by is = z or a * v1  + b * v2.
If we were to plug in real numbers. Let v1 have [1, 1, 1] and v2 have [2, 2, 2]. Let a be 1 and b be 2. 
The equation becomes:
    1 * [1, 1, 1] + 2 * [2, 2, 2] = z
    This is a linear combination.
"""
from quiz_3_1_7 import lin_comb
import numpy as np

def problem3_8_4(scalar: list, vlist: list) -> int:
    """
    Input: Scalar is a list of n lenght. vlist is a list of 2 vectors with 3 lengths of [x, y, z]. So vlist = [[x,y,z] [x,y,z]] 
    Output: The result of linear combo of scalar and vlist. So scalar[i] * vlist[i] + scalar[i] + vlist[i]
    """
    assert type(scalar) == type(np.array([]))
    assert type(vlist) == type(np.array([]))
    assert len(vlist) == 2 
    assert len(scalar) == 2 
    
    return np.sum([a * b for a,b in zip(scalar, vlist)])

    
