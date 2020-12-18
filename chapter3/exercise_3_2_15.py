"""
For each subproblem below, investigate whether the given vectors span R^2
If R^2 generator is missing a vector. Add an additional vector.

1.) [1,2], [3,4]
2.) [1,1], [2,2], [3,4]
3.) [1,1], [1,-1], [0,1]

Suppose that the general equation is the domain D contains n number of elements that's a span of generators for each R^2.
For each R^2 maps to a general equation of e sub 1 to n-1. Such that e of sub to n-1 starts from [1,...0] 
If Span is length 3, the general equation starts from [1, 1, 0], [1, 0, 1], [0, 1, 1]. Each maps to element of Span.

<<< from numpy import array

1.) [1, 2], [3 ,4] = 1[1,2] + 0[3,4]
                   = 0[1,2] + 1[3,4]
<<< a = array([[1, 2] [3,4]])
<<< g1 = (1*a[0]) + (0*a[1])
<<< [1,2]
<<< g2 = (0*a[0]) + (1*a[1])
<<< [3,4]

----
2.) [1, 1], [2, 2], [3, 3] 


<<< a = array([[1, 1], [2, 2], [3, 3]])
<<< g1 = (1*a[0]) + (1*a[1]) + (0*a[2])
<<< [3,3]
<<< g2 = (1*a[0]) + (0*a[1]) + (1*a[2])
<<< [4,4]
<<< g3 = (0*a[0]) + (1*a[1]) + (1*a[2])
<<< [5,5]


3.) [1,1], [1,-1], [0,1]

<<< a = array([[1, 1], [2, 2], [3, 3]])
<<< g1 = (1*a[0]) + (1*a[1]) + (0*a[2])
<<< [2,0]
<<< g2 = (1*a[0]) + (0*a[1]) + (1*a[2])
<<< [1,2]
<<< g3 = (0*a[0]) + (1*a[1]) + (1*a[2])
<<< [1,0]

"""


