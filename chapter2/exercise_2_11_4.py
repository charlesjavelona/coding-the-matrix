from module.vecutil import zero_vec 
"""
"""

def triangular_solve(row_list, label_list, bee):
    """
    Input: row_list is a triangular system of n-vectors.
           b is the result of each row of n-vectors.
    Output: The result of x[i] after implementing the backward subtitution on n-row.
    """
    import pdb
    pdb.set_trace()
    D = row_list[0].D
    x = zero_vec(D)
    for i in reversed(range(len(D))):
        if(len(D)):
            x[i] = bee[i]/row[i].F[i] 

        c = label_list[i]
        row = row_list[i]
        x[c] = (bee[i] - x * row)/row[i]
    return x

