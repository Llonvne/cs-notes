def make_adder(n):
    return lambda k : n + k

def curry2(f):
    """ return a new function h makes f(x,y) equals h(x)(y)
    """
    return lambda y:lambda x:f(x,y)

def add(a,b):
    return a + b



