from module.GF2 import one
from module.vec import Vec

def standard(D, external_one):

    assert one == external_one
    return [Vec(D, {k:external_one}) for k in D] 
