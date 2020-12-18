# insert at 1, 0 is the script path (or '' in REPL)
from resources.plotting import plot 

# (a + b)u = au + bu
# a & b are vectors
# u is a scalar

def add_vectors(v1, v2): return [x + y for x, y in zip(v1, v2)]

def mult_vector_by_scalar(v, s): return [e * s for e in v]


def segment(pt1, pt2, points=100):
    return [add_vectors(mult_vector_by_scalar(pt1, i/points), mult_vector_by_scalar(pt2, j/points)) for i in range(points) for j in range(points)] 

if __name__ == '__main__':
    pt1 = [3.5, 3]
    pt2 = [.5, 1]
    plot(segment(pt1, pt2), 5, 2)
