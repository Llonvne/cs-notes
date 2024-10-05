def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return True if temp < 60 or raining else False

def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return raining or (temp < 60)

def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

def is_prime(n):
    """
    >>> h = is_prime
    >>> h(10)
    False
    >>> h(7)
    True
    """
    i = 2
    while (i < n):
        if n % i == 0:
            return False
        i += 1
    return True
