
def list_dot(u, v):
    """
    Input: Equal length lists u and v of field elements
    Output: The dot product of u and v interpreted as vectors

    """
    return sum(a*b for a, b in zip(u,v))
