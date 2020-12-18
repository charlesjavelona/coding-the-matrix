from Vec import Vec

def neg(v):
    """
    Input: instance of Vec
    Output: Inverse of the instance of vec labels

    Example: Input: {'A': 1, 'B': 2} Output: {'A': -1, 'B': -2}
    """
    return Vec(v.D, {d: -v.get_item(d) for d in v.D}) 


if __name__ == '__main__':
    prin( neg(Vec({'A': 1, 'B': -2},{})))
