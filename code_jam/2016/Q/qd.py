import collections
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
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
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
    #fa = element; fb = C
    if fb == 1:
        return fa
    else:
        fc = []
        for fi in fa:
            if fi == '0':
                fc = fc + ['0' * len(fa)]
            else:
                fc = fc + [f(fa, fb - 1)]
        #print fc
        return ''.join(fc)

for i in range(1, 1 + input()):
    ca = raw_input().strip().split()
    ca = map(int, ca)
    if ca[0] == 1:
        cz = 1
    elif ca[0] == 2:
        cz = 2
    else:
        cb = '1' * ca[0]
        cc = []
        cz = ca[0]
        for j in range(ca[0]):
            cc.append(f(cb[:j] + '0' + cb[j+1:], ca[1]))
        print cc
        # for m in range(ca[0] - 1):
        #     for n in range(1,ca[0]):
        #         #print cc
        #         cd = bin(int(cc[m], 2) | int(cc[n], 2))[2:]
        #         #print cd
        #         cz = min(cz, cd.count('0'))
    if cz <= ca[2]:
        print "Case #{}: {}".format(i, cz)
    else:
        print "Case #{}: IMPOSSIBLE".format(i)
