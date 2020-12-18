import numpy as np
def diag(rc):
    """
    Input: rc, the number of square elements to make a diagonal matrix.
    Output: a matrix with diagonal content. 

    For example: 
    rc = 3 
    [1,0,0]
    [0,1,0]
    [0,0,1]
    """
    assert type(rc) == type(int()) 
    arr = np.empty([rc,rc])
    for i in range(len(arr)):
        l = list()
        for j in range(len(arr)):
            if(i == j):
                l.append(1)
            else:
                l.append(0)
        arr[i] = np.array(l)        
    return arr   


