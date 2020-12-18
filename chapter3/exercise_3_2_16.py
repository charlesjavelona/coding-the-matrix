"""
You are given vectors [1, 1, 1], [0.4, 1.3, -2.2]. 
Add one vector. Finally, express each of the standard generators for R^3 as a linear combo of the 3 vectors.


Let span equal to D with 3 vectors called k. 
k3 is randomly generated as vector [1, 2, 3].
D = {k1, k2, k3}
The standard generator of span D is e. Where e = [1, 1, 0] and shifts to the left until it becomes [0, 1, 1].

from numpy import array
a = array([[1,1,1], [0.4, 1.3, -2.2], [1, 2, 3]])
>>> a = array([[1, 1, 1], [0.4, 1.3, -2.2], [1, 2, 3]])
>>> g1 = (1*a[0]) + (1*a[1]) + (0*a[2])
>>> g2 = (1*a[0]) + (0*a[1]) + (1*a[2])
>>> g3 = (0*a[0]) + (1*a[1]) + (1*a[2])
>>> g1
array([ 1.4,  2.3, -1.2])
>>> g2
array([2., 3., 4.])
>>> g3
array([1.4, 3.3, 0.8])


## In this case, an actual generator could have been implemented and used such as list2vec instead of manually shifting the standard generator. 
"""
