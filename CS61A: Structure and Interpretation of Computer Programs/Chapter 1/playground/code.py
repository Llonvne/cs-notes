import math
from math import pi

""" First Python souce file"""
def divide_exact(n,d = 10):
    """
    Return the quotient and remainder of dividing N by D.

    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3

    >>> q, r = divide_exact(2013)
    >>> q
    201
    >>> r
    3
    """
    return n//d,n%d

def absolute_value(x):
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x

def naive_fibnacci(k):
    """Return the Kth elements of Fibonacci


    >>> first = naive_fibnacci(1)
    >>> first
    1
    >>> second = naive_fibnacci(2)
    >>> second
    1
    >>> third = naive_fibnacci(3)
    >>> third
    2
    """
    if k <= 1:
        return k
    else:
        return naive_fibnacci(k-1) + naive_fibnacci(k-2)

def fib(n):
    pred, curr = 1, 0
    k = 0
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

def search(f):
    x = 0
    while not f(x):
        x += 1
    return x

def inverse(f):
    """Return g(y) such that g(f(x)) -> x."""
    return lambda y : search(lambda x : f(x) == y)

def IF(c, t, f):
    if c():
        t()
    else:
        f()
        
def real_sqrt(x):
    if x > 0:
        return math.sqrt(x)
    else:
        return 0.0

def has_big_sqrt(x):
    return x > 0 and math.sqrt(x) > 10

def reasonabl(n):
    return n == 0 or 1 / n != 0

def area(r, k):
    """Return r * r * k"""
    assert r > 0, 'length must be positive'
    return r * r * k

hexagon_constant = 3 * math.sqrt(3) / 2

def area_square(r):
    return area(r,1)

def sum_naturals(n):
    """Sum the first N natural numbers

    >>> sum_naturals(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum(term, n):
    """ Sum the first N natural numbers after apply Term
    >>> sum(lambda x:x,5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def make_adder(n):
    """Return a function that takes one argument K and return K + N

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

