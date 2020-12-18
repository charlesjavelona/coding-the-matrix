from module.vec import Vec

def list2vec(L):
    """
    Input: List L of field elements
    Output: Return an instance of Vec with domain{0, 1, 2, ..., len(L)-1} such that v[i] = L[i] for each integer i in the domain

    Example: [0, 1, 2, 3, 4] -> {0, 1, 2, 3, 4}
    """
    return Vec({i for i in L}, {})


