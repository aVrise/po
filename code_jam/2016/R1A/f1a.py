import itertools
import sys
from sys import stdin, stdout
import functools

def f(fa, fb):
    #
    #print fb
    if len(fa) == 0:
        return fb
    if fa[0] >= fb[0]:
        fb = fa[0] + fb
    else:
        fb = fb + fa[0]
    return f(fa[1:], fb)

sys.setrecursionlimit(1500)
a = stdin.readlines()
#a = [[ x for x in u.strip().split() if x != '' ] for u in a ]

for i in range(1, 1 + int(a[0])):
    ca = a[i]
    cb = ca[0]
    print "Case #{}:".format(i), f(ca[1:], cb)
