def exercise_4_10_7():
    """
    Define g: R^2 -> R^>3 by g([x,y]) = [x,y,1]. Is g a linear function ?
    If so, prove it. If not, give a counter example.

    g([x,y]) = [x,y,1] is a linear function. However the output of [x,y,1] is incorrect because 1 is not a vector space in g. 
    A counter example is g([x,y,z]) = [x,y,1]. Such that it completes R^2 -> R^3. 
    
    """
    return ''


def exercise_4_10_8():
    """
    Define h:R^2 -> R^2 to be the funtion that takes a point [x,y] to it's reflection about the y-axis. Give an explicit(ie algebraic) definition of h.
    Is it a linear function.

    h: R^2 -> R^2 h([x,y]) = [-x,y]. According to the reflection of the y-axis. The y-coordinate remains the same. The x-coordinate is inverted to a positive or negative number. This is still considered a linear equation as h function inverts the coordinates based on the type of reflection. 

    h([x,y]) = (-xy) * (xy) => (-x, y)
    """
    return ''



def exercise_4_10_9():
    """
    In at least one of the examples in section 4.9.3 the function cannot be written as f(x) = M * x. Which one ? Demonstrate using numerical example that the function does not satisfy the properties L1 and L2 that define the linear function

    First, what is the properties of L1 and L2.
    L1 is for any vector u in the domain of f and any scalar a in F. f(au) = af(u)
    L2 is for any vector u and v in the domain of f. f(u+v) = f(u) + f(v)


    4.9.3.1
    Let s(.)be a function from R^2 to R^2 that scales the x-coordinates by 2.
    s([x,y]) = M * [x,y]
    """
    return ''

    Does this satisfy L1 ? M * [x,y]. Let [x,y] be x:
    """
