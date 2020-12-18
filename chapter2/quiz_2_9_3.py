
def average_of_vec(v):
    """
    Input: vector called v
    Output: An average of the entries of vector v

    Example: v = [1,2,3,4,5] average = [5] 
    """
    return sum(v)/len(v)


if name == '__name__':
    print(average_of_vec([1,2,3,4,5]))

