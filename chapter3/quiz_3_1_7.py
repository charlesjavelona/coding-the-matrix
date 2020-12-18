def lin_comb(vlist: list, clist: list) -> int:
    """
    Input: Two lists, vlist containing vectors, clists of the same length consisting of scalars.
    Output: The vector that is the linear combination of the vectors in vlist with corresponding coefficient clist.

    Example: vlist = [1, 2, 3, 4, 5], clist = [5, 4, 3, 2, 1] => [(1 * 5) + (2 * 4) + (3 * 3) + (4 * 2) + (5 * 1)]
    """
    assert len(vlist) == len(clist) 
    return sum([v * c for v,c in zip(vlist, clist)])


