def my_filter(L, num):
    """
    Input: List of numbers and a positive integer.
    Output: List of numbers not containing a multiple of num.
    Example: L = [1, 2, 3, 4, 5], num = 2. Return [1, 3, 5]
    Return: List

    Explanation: l%num produces a remainder. A remainder of l%num cannot be a multiple of num. Therefore, add l in the list.
    """
    return [l for l in L if (l%num)]


def my_lists(L):
    """
    input: List L of non-negative integers.
    output: A list of lists: For every element x in L create a list containing, 1,2...x.
    Example: Given [1, 2, 4] return [[1], [1,2], [1,2,3,4]]. Given [0] return [[]]

    """
    return [list(x for x in range(1,l+1)) for l in L ]

def my_function_composition(f,g):
    """
    Input: Two function f and g, represented as dictionaries such that g o f exists.
    Output: Dictionary tha represents (g o f)(x).
    Example: Given f = {0: 'a', 1: 'b'} and g = {'a' : 'apple', 'b', 'banana'}, return {0: 'apple', 1: 'bananna'}

    Explanation: (f o g)(x) -> g(f(x))
    """
    return {x: g[f[x]] for x in f for y in g }


def mySum(L):
    """
    Input: List of numbers
    Output: Sum of numbers in the list
    """
    current = 0
    for x in L:
        current += x 
    return current    


def myProduct(L):
    """
    Input: List of numbers
    Output: Product of numbers in the list
    """
    current = 1 
    for x in L:
        current *= x 
    return current    


def myMin(L):
    """
    Input: List of numbers
    Output: Minimum of number in the list
    """
    current = L[0] 
    for x in L:
        current = x if(x < current) else current 
    return current    



def myConcat(L):
    """
    Input: List of sets 
    Output: strings in L 
    """
    current = '' 
    for x in L:
        current += x 
    return current    

def myUnion(L):
    """
    Input: List of sets 
    Output: Union of all sets in L 
    """
    current = set() 
    for x in L:
        current = current.union(x) 
    return current    






