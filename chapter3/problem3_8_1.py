
def vec_select(veclist:list) -> list:
    """
    Input: a list called veclist of vectors over the same domain, and an element k of the domain.
    Output: the sublist of veclist consisting of the vectors v in veclist where v[k] is zero.

    Example: veclist = [0, 1, 2, 3, 4, 5, 0, 9, 1, 3, 0, 3, 0]  returns [0, 0, 0]
    """
    assert type(veclist) == type([])
    veclist.sort()
    return [ i for i in veclist if i == 0 ]


def vec_sum(veclist:list, d: set) -> int:
    """
    Input: a list called veclist of vectors, and a set D that is common domain of these vectors
    Output: The vector sum of the vectors in veclist

    Example: veclist = [0, 1, 2, 3, 4], d = {one, two, three} returns the sum of veclist, 10.

    Assumption: List of vectors is a 1d array. Otherwise, a 2d array must be flat in order to find the sum.
    **Note: Not sure why d is included in this set. Presuming this is a typo.
    """
    assert type(veclist) == type([])
    assert type(d) == type(set)
    return sum(veclist) 

