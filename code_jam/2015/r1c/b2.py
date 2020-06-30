from fractions import gcd
import functools

class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

@memoized
def g(ga, gb, gc):
    if gb == -1:
        return 0
    elif :
        return 0
    else:
        return gc*g(ga, gb-1, gc) + (1 - gc)*g(ga, gb-1, gc)

def f(fa, fb):
    fz = 1
    for fi in fa:
        fz *= fb[fi] 
        if fz < 10**(-7):
            return 0
    return fz

for i in range(1, 1 + input()):
    ca = map(int, raw_input().split())
    cb = raw_input()
    cc = raw_input()
    cd = set(cb)
    ce = set(cc)
    cf = list(cb)
    cg = list(cc)
    cz = 0.0
    cx = 0.0
    cy = 0.0

    if len(cd|ce) > len(cd):
        cz = 0.0
    else:
        for ci in range(1, len(cg)):
            if cg[ci:] == cg[0:len(cg[ci:])]:
                break
        else:
            ci = 0
        cmax = (ca[2] - ca[1])/(len(cg) - ci) + 1

        cz = f()
    print "Case #{}: {}".format(i, cz)
        