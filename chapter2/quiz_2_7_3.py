from Vec import Vec

def scalar_mul(v, alpha):
    """
    Input: Vec instance, scalar alpha
    Output: New instance of vec including scalar vector product alpha times v
    Example: scalar_mul(v, 2) 
             scalar_mul(v, 2).f === {'A': 2, 'C': 0, 'B': 4}
    """
    return Vec(v.D, {k:v.get_item(k) * alpha for k in v.D})


if __name__ == '__main__':
    print(scalar_mul(Vec({'A': 1, 'B': 0, 'C': 4}, {}), 2))

