def make_adder(n):
    def adder(k):
        return k + n
    return adder

def square(x):
    return x * x

def triple(x):
    return 3 * x

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h
