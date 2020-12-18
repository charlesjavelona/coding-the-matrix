def problem_2_14_1(v, u):
    """
    Find the vectors for v + u, v - u, and 3v - 2u
    <<< v = [-1, 3], u = [0, 4]
    <<< from numpy import array
    <<< v + u 
    <<< [-1, 7]
    <<< v - u 
    <<< [-1, -1]
    <<< (3*v) - (2*u)
    <<< [-3, 1]
    """
    pass


def problem_2_14_2(v, u):
    """
    Find the vectors v + u, v - u, 2v - u, v + 2u
    <<< v = [2, -1, 5], u = [-1, 1, 1]
    <<< v + u
    <<< [x+y for x, y in zip(v, u)]
    <<< v - u 
    <<< [x-y for x, y in zip(v, u)]
    <<< 2v - u
    <<< [x-y for x, y in zip((2 * i for i in v), u)]
    <<< v + 2u
    <<< [x+y for x, y in zip(v, (2 * i for i in  u))]
    """
    pass

def problem_2_14_3(v, u):
    """
    v = [0, one, one], u = [one, one, one] over GF(2)
    Find v + u, v + u + u
    from resources.GF2 import one
    <<< v + u
    <<< [x + y for x, y in zip(v, u)]
    <<< [one, 0, 0]
    <<< v + u + u
    <<< l = [x + y for x, y in zip(v, u)]
    <<< l
    <<< [one, 0, 0]
    <<< l = [x + y for x, y in zip(l, u)]
    <<< l
    <<< [0, one, one]
    """
    pass

def problem_2_14_4(a_list, u):
    """
    from module.GF2 import one
    **All 1's are one**
    a = 1100000, b = 0110000, c = 0011000, d = 0001100, e = 0000110, f = 0000011
    For each vector u, find a subset of the above vectors sum is u or report no tables exist.
    <<< a = [1,1,0,0,0,0,0]
    <<< b = [0,1,1,0,0,0,0]
    <<< c = [0,0,1,1,0,0,0]
    <<< d = [0,0,0,1,1,0,0]
    <<< e = [0,0,0,0,1,1,0]
    <<< f = [0,0,0,0,0,1,1]
    <<< a_list = [a, b, c, d, e, f]
    <<< u = [0,0,1,0,0,1,0]
    <<<problem_2_14_4(a_list, u)
    <<< False 
    <<< u = [0,1,0,0,0,1,0]

    ** Works with problem_2_14_5. Answers are all false.
    """
    is_true = False
    for l in a_list:
        for k in a_list:
            if(l == k): continue
            if([x+y for x,y in zip(l,k)] == u):
                is_true = True
                break
    return is_true 


def problem_2_14_6():
    """
    Satisfy the following with the vector = [x sub1, x sub2, x sub3, x sub4] over GF(2)

    [one, one, 0, 0] * x = 1
    [one, 0, one, 0] * x = 1
    [one, one, one, one] * x = 1
    x + [one, one, one, one] = 1

    <<< a = [one, one, 0, 0] 
    <<< b = [one, 0, 0, 0]
    <<< sum([x * y for x,y in zip(a,b)])         
    <<<
    <<< a = [one, 0, one, 0]
    <<< b = [one, 0, 0, 0]
    <<< sum([x * y for x,y in zip(a,b)])

    <<< a = [one, one, one, one]
    <<< b = [one, 0, 0, 0]
    <<< sum([x * y for x,y in zip(a,b)])

    x + [one, one, one, one]
    <<< a = [one, one, one, one]
    <<< b = [0, one, one, one]
     <<< sum([x + y for x,y in zip(a,b)])
    """
            

