import itertools
import sys
from sys import stdin, stdout
import functools

def f(fa, fb, fc, fd):
    #
    fd[fb] = -1
    fc = fc + [fb]
    #print fa, fd
    #print fc, fd
    if fa[fb] not in fc:
        return f(fa, fa[fb], fc, fd)
    elif fa[fb] == fc[0]:
        return len(fc)
    elif fa[fb] == fc[-2]:
        return len(fc) + 1 * (fc[0] in fd) + 1 * (fc[-1] in fd)
    else:
        return len(fc) + 1 * (fc[0] in fd) + 1 * (fc[-1] in fd) - 1
    #else:
        #print fc, fd
        #return len(fc) + 1 * (fc[0] in fd) + 1 * (fc[-1] in fd)
def g(ga, gb, gc):



a = stdin.readlines()
a = [[ int(x) for x in u.strip().split() if x != '' ] for u in a ]

for i in range(1, 1 + int(a[0][0])):
    ca = a[2 * i - 1][0]
    cb = [ x - 1 for x in a[2 * i][:]]
    #print cb
    cmax = 0
    for j in range(ca):
        cc = []
        cd = cb[:]
        temp = f(cb, j, cc, cd)
        if temp > cmax:
            cmax = temp
    if cmax > ca:
        cmax = ca
    print "Case #{}:".format(i), cmax
