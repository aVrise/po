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
def f(fa, fb):
    if len(fa) == 1:
        return long(fa[0])
    else:
        return long(fa[0]) * fb ** (len(fa) - 1) + f(fa[1:], fb)

#def g(ga):
#    if ga % 2==0 : return 2
#    for gi in range(3, long(ga ** 0.5) + 1, 2):   # only odd numbers
#        if ga % gi==0:
#            return gi
#    return 0

def g(ga, gb):
    return (ga * ga + 1) % gb

def h(ha):
    hx, hy, d, i = 2, 2, 1, 1
    while d == 1:
        x = g(hx, ha)
        y = g(g(hy, ha), ha)
        d = gcd(abs(x - y), ha)
        i += 1
        if i > 500: return 0
    if d == ha:
        return 0
    else:
        return d


m = 0
print "Case #{}:".format(input())
i = [int(x) for x in raw_input().strip().split()]
j = 2 ** (i[0] - 1) + 1
while j <  2 ** (i[0]):
#for j in xrange(2 ** (i[0] - 1) + 1, 2 ** (i[0]), 2):
    l = [long(bin(j)[2:])]
    j += 2
    for k in range(2, 11):
        l.append(h(long(int(str(l[0]), k))))
        if l[-1] == 0:
            break
    if l[-1] == 0:
        continue
    else:
        m += 1
        for n in l:
            print n,
        print
    if m == i[1]:
        break
