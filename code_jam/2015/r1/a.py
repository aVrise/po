import sys

def f(fa):
    if len(fa) == 1:
        return 0
    else:
        return max(fa[0] - fa[1], 0) + f(fa[1:])

def g(ga, gb):
    if len(ga) == 1:
        return gb
    else:
        gb = max(gb, ga[0] - ga[1])
        return g(ga[1:], gb)
def h(ha, hb):
    if len(ha) == 1:
        return 0
    else:
        return min(ha[0], hb) + h(ha[1:], hb)

for i in range(1, 1 + input()):

    sys.setrecursionlimit(2000)
    ca = input()
    cb = raw_input().split()
    cc = map(int, cb)

    cz = f(cc)
    cy = h(cc, g(cc, 0))

    print("Case #{}: {} {}".format(i, cz, cy))
