import itertools
from sys import stdin, stdout
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
def f(fa,fb):
    #fa = list[K], fb = K
    if len(fa) == 0:
        if fb == 0:
            return 1.0
        else:
            return 0.0
    elif fb < 0:
        return 0.0
    else:
        return fa[0] * f(fa[1:],fb - 1) + (1 - fa[0]) * f(fa[1:], fb)

a = stdin.readlines()
a = [[ float(x) for x in u.strip().split() if x != '' ] for u in a ]
for i in range(1, 1 + int(a[0][0])):
    l = list(itertools.combinations(a[2 * i], int(a[2 * i - 1][1])))
    print "Case #{}: {}".format(i, max(map(lambda x: f(x, int(a[2 * i - 1][1])/2), l)))
